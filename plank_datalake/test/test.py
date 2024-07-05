from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from faker import Faker
import base64

fake = Faker()

chromedriver_path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome()

def crip(text):
    crip = base64.b64encode(text.encode()).decode()
    return crip



def formCustomer():

    driver.get("http://127.0.0.1:8000/customer/")
    time.sleep(3)
    str_name = driver.find_element("xpath", '//*[@id="id_str_name"]')
    str_cnpj = driver.find_element("xpath", '//*[@id="id_str_cnpj"]')
    str_address = driver.find_element("xpath", '//*[@id="id_str_address"]')
    str_telefone = driver.find_element("xpath", '//*[@id="id_str_telefone"]')
    str_email = driver.find_element("xpath", '//*[@id="id_str_email"]')
    str_site = driver.find_element("xpath", '//*[@id="id_str_site"]')
    str_linkedin_profile = driver.find_element("xpath", '//*[@id="id_str_linkedin_profile"]')
    str_contact = driver.find_element("xpath", '//*[@id="id_str_contact"]')
    dth_create = driver.find_element("xpath", '//*[@id="id_dth_create"]')
    str_finance_complement = driver.find_element("xpath", '//*[@id="id_str_finance_complement"]')
    str_comments = driver.find_element("xpath", '//*[@id="id_str_comments"]')

    str_name.send_keys(fake.company())
    str_cnpj.send_keys('52.065.856/0001-49')
    str_address.send_keys(fake.address())
    str_telefone.send_keys(fake.phone_number())
    str_email.send_keys(fake.email())
    str_site.send_keys(fake.url())
    str_linkedin_profile.send_keys(fake.url())
    str_contact.send_keys(fake.name())
    dth_create.send_keys(fake.date_time_this_century().strftime('%Y-%m-%d %H:%M:%S'))
    str_finance_complement.send_keys(fake.text(max_nb_chars=100))
    str_comments.send_keys(fake.text(max_nb_chars=100))

    
    time.sleep(3)
    # <button type="submit" class="btn btn-primary mt-3">Cadastrar</button>
    button = driver.find_element('xpath',"/html/body/div/div/div/div/div/form/button")
    button.send_keys(Keys.ENTER)
    time.sleep(3)

    url_arg = str(driver.current_url).split('/')[-1]
    for i in range(1, 5):
        formUser(url_arg)
    
    time.sleep(3)
    formSistema(url_arg)


def formUser(url_arg):
    url = f"http://127.0.0.1:8000/signup/{url_arg}"
    driver.get(url)
    time.sleep(3)

    first_name = driver.find_element("xpath", '//*[@id="id_first_name"]')
    first_name.send_keys(fake.first_name())

    last_name = driver.find_element("xpath", '//*[@id="id_last_name"]')
    last_name.send_keys(fake.last_name())

    str_cpf = driver.find_element("xpath", '//*[@id="id_str_cpf"]')
    str_cpf.send_keys('000.000.000-00')

    str_telefone = driver.find_element("xpath", '//*[@id="id_str_telefone"]')
    str_telefone.send_keys('11 999999999')

    str_cargo = driver.find_element("xpath", '//*[@id="id_str_cargo"]')
    str_cargo.send_keys(fake.job())

    str_address = driver.find_element("xpath", '//*[@id="id_str_address"]')
    str_address.send_keys(fake.address())

    email = driver.find_element("xpath", '//*[@id="id_email"]')
    email.send_keys(fake.email())

    password = driver.find_element("xpath", '//*[@id="id_password"]')
    password.send_keys(fake.password()[10:])

    button = driver.find_element('xpath',"/html/body/div/div/div/div/div/div/div/div[2]/form/div[10]/div/button")
    button.send_keys(Keys.ENTER)

    time.sleep(3)

def formSistema(url_arg):
    for system in ('Salesforce','SAP','BCS','ORACLE','TOTVS'):
        url = f"http://127.0.0.1:8000/system/{url_arg}"
        driver.get(url)
        time.sleep(3)

        str_title = driver.find_element("xpath", '//*[@id="id_str_title"]')
        str_title.send_keys(system)

        str_desc = driver.find_element("xpath", '//*[@id="id_str_desc"]')
        str_desc.send_keys('Sistema de teste')
        button = driver.find_element('xpath',"/html/body/div/div/div/div/div/div/form/button")
        button.send_keys(Keys.ENTER)
        time.sleep(3)
        url_arg = str(driver.current_url).split('/')[-1]
        formDataSet(url_arg)

def formDataSet(url_arg):
    for system in ('Cadastro','Transacoes','Tecnologia','Inventario','Recursos Humanos'):
        url = f"http://127.0.0.1:8000/dataset/{url_arg}"
        driver.get(url)
        time.sleep(3)
        str_title = driver.find_element("xpath", '//*[@id="id_str_title"]')
        str_title.send_keys(system)
        str_desc = driver.find_element("xpath", '//*[@id="id_str_desc"]')
        str_desc.send_keys('Dataset de teste')
        button = driver.find_element('xpath',"/html/body/div/div/div/div/div/div/form/button")
        button.send_keys(Keys.ENTER)
        time.sleep(3)


for i in range(1, 5):
    formCustomer()

time.sleep(5)


