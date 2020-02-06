import requests


url = "https://cl.fiitt.xyz/post.php?atc_usesign=1&atc_convert=1&atc_autourl=1&atc_title=Re%3A%5B%D4%AD%B4%B4%5D%D4%BC%C5%DA01%C4%EA%B5%C4%B3%A4%CD%C8%C3%C3%D7%D3%A3%AC%B1%C6%BD%F4%CB%AE%B6%E0%A3%AC%BC%D0%B5%C3%BC%A6%B0%CD%CC%AB%CA%E6%B7%FE%C1%CB%5B38P%5D&atc_content=1024&step=2&action=reply&fid=16&tid=3801737&atc_attachment=none&pid=&article=&verify=verify"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
    "cookie": "UM_distinctid=16f27077692b-0d1c98c18bec3d-6701434-100200-16f2707769313; __cfduid=ddff1a08dda0532f11b38d51fc205c4901580875187; PHPSESSID=b8gkibv9324v7t9bdc2v618g74; 227c9_ck_info=%2F%09; 227c9_winduser=AAVQVlcFO1cACwBUBFVWWFdXAwxUVVFQB1YMCVpQU1cIAFEABFBSaw%3D%3D; 227c9_groupid=8; 227c9_ipfrom=2e7f75bbf3f3e0f76eea2ea927717bda%09Unknown; 227c9_postReplyLastData=37589521024; 227c9_lastvisit=0%091580891238%09%2Fpost.php%3Ffid%3D8; CNZZ"
}
res = requests.post(url, headers=header)
print(res.content.decode("gbk"))