#coding:utf-8
import secrets
from hashlib import sha256
import utils



G_X = 55066263022277343669578718895168534326250603453777594175500187360389116729240
# BASE_Y = 111369311037667457822445869299419316870247801668819120014212655173383442957026
G_Y = 32670510020758816978083085130507043184471273380659243275938904335757337482424

G = (G_X, G_Y)#基点
# 有限域的阶
P = 115792089237316195423570985008687907853269984665640564039457584007908834671663
# 椭圆曲线的阶
N = 115792089237316195423570985008687907852837564279074904382605163141518161494337



def generate_key():
    private_key = int(secrets.token_hex(32), 16)
    public_key = utils.elliptic_multiply(private_key, G)
    # print("Private Key: ",private_key)
    # print("Public Key: " ,public_key)
    return private_key, public_key

prikey, pubkey = generate_key()

print('真实公钥：',pubkey)

def hash(message):
    hashed_message = sha256(message.encode('utf-8')).hexdigest()
    # hashed_message = sha256(hashed_message.encode('utf-8')).hexdigest()#双重哈希
    return int(hashed_message, 16)



def sign(private_key, message):#私钥签名
    e = hash(message)#哈希
    k = secrets.randbelow(P)#0~P的随机数
    # k=12581384025608555250890351613719061476129424215689402246915303910451212003013
    random_point = utils.elliptic_multiply(k, G)#P点=k*G
    r = random_point[0] % P
    s = utils.mod_inverse(k, N) * (e + r*private_key) % N#用私钥进行签名

    return (r, s)#以元组形式存在的签名




message = "hello,world!"
signature = sign(prikey, message)

print("签名: ",signature)


# #y^2=x^3+7
# A = 0
# B = 7
'''根据签名内容反推出公钥：'''
def deduce_pubkey_fromsign(signature,message):
    r=signature[0]
    s=signature[1]
    x = r % P
    y2=((x**3)+7)
    y=utils.Tonelli_Shanks(y2,P)


    e = hash(message)
    POINT_1=(x,y)
    POINT_2=(x,P-y)

    #y1:
    skG=utils.elliptic_multiply(s%N,POINT_1)
    eG=utils.elliptic_multiply(e%N,G)
    negeG=(eG[0],P-eG[1])
    skGeG=utils.elliptic_add(skG,negeG)
    pub1=utils.elliptic_multiply(utils.mod_inverse(r,N),skGeG)

    # y2:
    skG=utils.elliptic_multiply(s%N,POINT_2)
    skGeG=utils.elliptic_add(skG,negeG)
    pub2=utils.elliptic_multiply(utils.mod_inverse(r,N),skGeG)
    return pub1,pub2



pub1,pub2=deduce_pubkey_fromsign(signature,message)
print('根据签名和消息，推测出公钥：')
print('可能公钥1：',pub1)
print('可能公钥2：',pub2)

