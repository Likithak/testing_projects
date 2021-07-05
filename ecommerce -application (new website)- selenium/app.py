from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
import logging
import time

# basic configuration of log_file format and level
logging.basicConfig(
    filename="class.log",
    filemode="w",
    format="%(asctime)s :: %(message)s",
    level=logging.INFO,
)
username = "kanlikitha99@gmail.com"
with open ('password.txt','r') as file:
        password = file.read()

class Ecommerce:
    """Automating a E-commerce website place an order with Ecommerce class"""

    def __init__(self):
        '''Intialising Chrome drive for automating '''
        self.driver = Chrome()
        self.driver.implicitly_wait(10)
        self.action=ActionChains(self.driver)
        logging.info('webdriver of chorme has been configured')
    
    def get_url(self):
        '''Browser geting respective url '''
        self.driver.get("http://automationpractice.com/index.php")
        logging.info('Getting ecommerce home page')

    def login(self):

        signin = self.driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()

        Emailid = self.driver.find_element_by_id("email")
        Emailid.send_keys(username)

        password_textbox = self.driver.find_element_by_id("passwd")
        password_textbox.send_keys(password)

        button = self.driver.find_element_by_id("SubmitLogin")
        button.click()
        print("login successfully")
        logging.info("login sucessfully to my_store website")
    
    def tshirt(self):
        #Picking a choice
        women_icon=self.driver.find_element_by_xpath("/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[1]/a")
        self.action.move_to_element(women_icon).perform()
        tshirt=self.driver.find_element_by_xpath("/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[1]/ul/li[1]/ul/li[1]/a").click()
        logging.info('In women section T-shirt was selected')
        time.sleep(2)
        #Getting product details
        details=self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[2]/ul/li/div/div[2]/h5/a").click()
        logging.info('details line executed')
        time.sleep(3)
        quatity_increase = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div/div[4]/form/div/div[2]/p[1]/a[2]/span").click()
        logging.info("quatity_increase line executed")
        time.sleep(3)
        colour=self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div/div[4]/form/div/div[2]/div/fieldset[2]/div/ul/li[2]/a").click()
        time.sleep(3)
        logging.info("colour")
        L_size = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div/div[4]/form/div/div[2]/div/fieldset[1]/div/div/select/option[text()='L']").click()
        time.sleep(3)
        logging.info("l_size")
        #adding product to the cart
        cart = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div/div[4]/form/div/div[3]/div[1]/p/button/span").click()
        time.sleep(3)
        logging.info("cart")
        proceed = self.driver.find_element_by_xpath("/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/a/span").click()
        time.sleep(3)
        logging.info("proceed")
        next_proceed = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/p[2]/a[1]/span").click()
        time.sleep(3)
        logging.info("next_proceed")
        address= self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/form/p/button/span").click()
        time.sleep(3)
        logging.info("address line executed")
        agree = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/form/div/p[2]/div/span/input").click()
        logging.info("agree")
        shipping= self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/form/p/button/span").click()
        logging.info("shipping")
        payment_proceed = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div[3]/div[2]/div/p/a").click()
        logging.info("payment_proceed")
        payment_check = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/form/p/button/span").click()
        logging.info("last line is executed")   
    '''
    def whishlist(self):
        women_icon=self.driver.find_element_by_xpath("/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[1]/a")
        self.action.move_to_element(women_icon).perform()
        tshirt=self.driver.find_element_by_xpath("/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[1]/ul/li[1]/ul/li[1]/a").click()
        details=self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[2]/ul/li/div/div[2]/h5/a").click()
        add_to_whishlist=self.find_element_by_xpath("").click()
        print("You must be logged in to manage your wishlist")
    '''
browser=Ecommerce()
browser.get_url()  
browser.login() 
# browser.tshirt()
# browser.whishlist()


