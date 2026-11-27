"""Guarda (ou repõe) a pasta de trabalho encriptada no repositório das páginas, para sobreviver ao fim do contentor.
  PAGE_PW=... python3 tools/snapshot.py save     -> /home/user/pedromja.github.io/_src/carros-work.tar.gz.enc
  PAGE_PW=... python3 snapshot.py restore <ficheiro.enc> <destino>"""
import os,sys,io,tarfile,base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
def key(pw,salt): return PBKDF2HMAC(hashes.SHA256(),32,salt,600000).derive(pw.encode())
pw=os.environ['PAGE_PW']
if sys.argv[1]=='save':
    W=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); out='/home/user/pedromja.github.io/_src/carros-work.tar.gz.enc'
    buf=io.BytesIO()
    import re,glob
    # 27/11: fora da cópia os duplicados dos pacotes diários (já copiados para tracker/inbox/) e as versões antigas
    # de ficheiros que só se usam uma vez (excel_data_*, anuncios_*): fica sempre o mais recente.
    ib=os.path.join(W,'tracker','inbox')
    keep=set()
    for pat in ('excel_data_2026-*_v8.json','anuncios_2026-*.json'):
        f=sorted(glob.glob(os.path.join(ib,pat)))
        keep.update(os.path.basename(x) for x in f[-2:])
    def flt(ti):
        n=ti.name
        if n.endswith(('_full.html','.log')): return None
        if re.search(r'/tracker/inbox/grok_\d{4}-\d\d-\d\d/(excel_data_[^/]*\.json|anuncios\.json|historico_precos\.csv|cayenne_e(/.*)?)$',n): return None
        m=re.search(r'/tracker/inbox/((excel_data_2026-[^/]*_v8|anuncios_2026-[^/]*)\.json)$',n)
        if m and m.group(1) not in keep: return None
        return ti
    with tarfile.open(fileobj=buf,mode='w:gz') as t: t.add(W,arcname='carros-work',filter=flt)
    salt=os.urandom(16); iv=os.urandom(12); os.makedirs(os.path.dirname(out),exist_ok=True)
    open(out,'wb').write(salt+iv+AESGCM(key(pw,salt)).encrypt(iv,buf.getvalue(),None)); print(out,os.path.getsize(out))
else:
    b=open(sys.argv[2],'rb').read(); salt,iv,ct=b[:16],b[16:28],b[28:]
    with tarfile.open(fileobj=io.BytesIO(AESGCM(key(pw,salt)).decrypt(iv,ct,None)),mode='r:gz') as t: t.extractall(sys.argv[3],filter='data')
    print('reposto em',sys.argv[3])
