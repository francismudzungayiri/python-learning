import requests
from bs4 import BeautifulSoup


amazon_url = 'https://www.amazon.com/Intelligent-Wireless-Charger-Bluetooth-Charging/dp/B0C535NZQ8/ref=sr_1_22_sspa?_encoding=UTF8&content-id=amzn1.sym.5b5b28b3-a1ac-480e-bf55-5b98e8879363&dib=eyJ2IjoiMSJ9.Ifv54RCe_3m_LIKifD4ToRWhxhSJbdyz7beId2X1WhSfVEQeRPK95rop8h_Vs32vaUs9bGdH5uxV_JCsFyiPJolFHtqq3NNwubI6S65MOVlYwFf9L00F1qDrLj1YU97ehW6F7pb79ssajDWwk3pxOJ0g7A8Vjz0fRDS_QriL-cziUYT7LKpcfbUDWpznoP-uqiqYuFHMOFUhGOHbpynhgANJ5vpVhgebo7wZDAk_0moYI8W4FN5AZf57oX_JFhpPNXYHa2kru_RC4vXXuMffBzGv69jPsK7cMmtgxgx6TQo.Ez9HJjR1KtlZUJ0V9Qvpn_Zaw_BQZGedeYJC8ktyBcA&dib_tag=se&keywords=smart%2Bhome&pd_rd_r=a172555a-5d17-4de9-80cf-674c8eaf2743&pd_rd_w=teoXS&pd_rd_wg=zEury&pf_rd_p=5b5b28b3-a1ac-480e-bf55-5b98e8879363&pf_rd_r=02JNAKFBV7DJQC8QPA8G&qid=1737396088&sr=8-22-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&th=1'
response = requests.get(amazon_url)

soup = BeautifulSoup(response.text, 'html.parser')


prices = soup.findAll(name='span', class_='a-price-whole')
item_prices = [int(price.get_text().split('.')[0]) for price in prices]
print(max(item_prices))