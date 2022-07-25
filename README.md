# Deduce-public-key-from-signature
#从签名推断公钥



由签名值s =((1 +d_A)^{-1}·(k-r·d_A))mod n, 公钥P_A =d_A·G 可推得 P_A = (r+s)^{-1}(kG-sG) kG=(x1,y1)可由式 r =(e+x1)mod n求出 (kG)_x =x1 =(r-e) mod n
