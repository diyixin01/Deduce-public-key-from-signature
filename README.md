# Deduce-public-key-from-signature
# ECDSA原理


# 密钥的产生
每个签名者需要产生一个密钥对，包括一个私钥和一个公钥。签名者，假设是Bob，通过以下步骤产生上述两个密钥：


1.选择随机整数d，d在1到n-1之间

2.计算Q=dG，得到一个曲线上的解点。


3.Bob的公钥是Q，私钥是d
# 签名产生
1、选择一条椭圆曲线Ep(a,b)，和基点G；


2、选择私有密钥k（k<n，n为G的阶），利用基点G计算公开密钥K=kG；


3、产生一个随机整数r（r<n），计算点R=rG；


4、将原数据和点R的坐标值x,y作为参数，计算SHA1做为hash，即Hash=SHA1(原数据,x,y)；


5、计算s≡r - Hash * k (mod n)


6、r和s做为签名值，如果r和s其中一个为0，重新从第3步开始执行


# 签名验证
1、接受方在收到消息(m)和签名值(r,s)后，进行以下运算


2、计算：sG+H(m)P=(x1,y1), r1≡ x1 mod p。


3、验证等式：r1 ≡ r mod p。


4、如果等式成立，接受签名，否则签名无效。



![image](https://user-images.githubusercontent.com/75195549/181193670-593fd30b-66fa-4338-bba2-856781fe89af.png)



# 代码函数说明
# 判断二次（非）剩余


![image](https://user-images.githubusercontent.com/75195549/181209384-69c08201-a316-4741-9448-0d735799bee9.png)


# 求解二次剩余


![image](https://user-images.githubusercontent.com/75195549/181209545-3aeaa3c8-fe22-4096-bc05-843fd95cd389.png)



# 求逆元


![image](https://user-images.githubusercontent.com/75195549/181209931-dd278e2d-99ba-4791-af88-d454a49574a8.png)



# 椭圆曲线参数



![image](https://user-images.githubusercontent.com/75195549/181210012-c0d49129-c88a-4f9d-97e8-ea286f874bfd.png)




# 椭圆曲线上的加法
def add(P, Q): 
# 椭圆曲线上的乘法
def multi(P, Q): 


# 生成公私钥对


![image](https://user-images.githubusercontent.com/75195549/181210194-6d3174d8-efba-432e-b675-240fa966eb80.png)




# 从签名反推出公钥


![image](https://user-images.githubusercontent.com/75195549/181210257-e2aa2336-72dc-4488-9e7e-b94e6f3a208d.png)






# 结果展示

![image](https://user-images.githubusercontent.com/75195549/181208435-7f4c8aef-461f-435f-8a06-e43b1406b73a.png)


