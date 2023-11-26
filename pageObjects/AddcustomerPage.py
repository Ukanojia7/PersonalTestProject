import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer:
    # Add customer page
    lnkCustomer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomer_MenuItem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddNew_xpath = "//a[normalize-space()='Add new']"

    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_ID = "FirstName"
    txtLastName_Id = "LastName"

    rdMaleGender_ID = "Gender_Male"
    rdFemaleGender_ID = "Gender_Female"

    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"

    txtCustomerRoles_xpath = "(//div[@role='listbox'])[2]"
    listItemAdministrators_xpath = "//li[normalize-space()='Administrators']"
    listItemRegistered_xpath = "//li[@id='69f58606-532f-45a1-a2c4-2d33526b0536']"
    listItemGuests_xpath = "//li[normalize-space()='Guests']"
    listItemVendors_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[5]"

    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"

    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menu_xpath).click()

    def clickOnCustomersMenuItems(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_MenuItem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
        time.sleep(2)
        #self.listitem = self.driver.find_element(By.XPATH, self.listItemVendors_xpath).click()

        if role == 'Registered':
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.listItemRegistered_xpath)

        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.listItemAdministrators_xpath_xpath)

        elif role == 'Guests':
            #self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_listbox']/li[3]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.listItemGuests_xpath)

        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.listItemVendors_xpath)

        else:
            self.listitem = self.driver.find_element(By.XPATH, self.listItemGuests_xpath)
        time.sleep(1)

        self.listitem.click()
        #self.driver.execute_script("argument[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMaleGender_ID).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFemaleGender_ID).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_ID).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.txtFirstName_ID).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.txtLastName_Id).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)
    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()



