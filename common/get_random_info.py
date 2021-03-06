from faker import Faker

fake = Faker(locale='zh-CN')


class RandomPerson():
    '''-----------个人信息类-------------'''

    def rp_name(self):
        """姓名"""
        return fake.name()

    def rp_ssn(self):
        """身份证"""
        return fake.ssn()

    def rp_user_name(self):
        """用户名"""
        return fake.user_name()

    def rp_password(self):
        """密码:
        参数选项：length：密码长度；special_chars：是否能使用特殊字符；digits：是否包含数字；upper_case：是否包含大写字母；lower_case：是否包含小写字母。
        默认情况：length=10, special_chars=True, digits=True, upper_case=True, lower_case=True"""
        return fake.password()

    def rp_phone_number(self):
        '''电话'''
        return fake.phone_number()

    def rp_job(self):
        '''工作'''
        return fake.job()

    def rp_simple_profile(self):
        '''简略个人信息，包括用户名，姓名，性别，地址，邮箱，出生日期'''
        return fake.simple_profile()

    def rp_profile(self):
        '''详略个人信息，比简略个人信息多出公司名、血型、工作、位置、域名等等信息'''
        return fake.profile()

    def rp_email(self):
        """email"""
        return fake.email()

    def rp_element(self):
        """随机字母"""
        return fake.rp_element()


class RandomData():
    '''----------数据类型-----------'''

    def rd_pystr(self, length=20):
        """自定义长度的随机字符串,默认长度为20"""
        return fake.pystr(min_chars=None, max_chars=length)

    def rd_pyint(self):
        """随机整数"""
        return fake.pyint()

    def rd_digit(self):
        """生成0~9随机数"""
        return fake.rd_digit()

    def rd_int(self):
        """随机数字，默认0~9999，可以通过设置min,max来设置"""
        return fake.rd_int(min=1, max=9999)

    def rd_pyfloat(self):
        """left_digits=5 #生成的整数位数,right_digits=2 #生成的小数位数,positive=True #是否只有正数"""
        return fake.rd_pyfloat(left_digits=5, right_digits=2, positive=True)

    def rd_str(self, goodname):
        return goodname + self.rd_pystr(5)


class RandomAdderss():
    '''------------地址信息类-----------'''

    def ra_country(self):
        """随机国家"""
        return fake.country()

    def ra_province(self):
        """随机省份名"""
        return fake.province()

    def ra_city_name(self):
        """随机城市名"""
        return fake.city_name()

    def ra_postcode(self):
        """随机邮编"""
        return fake.postcode()

    def ra_street_name(self):
        """随机街道名"""
        return fake.street_name()

    def ra_address(self):
        """随机地址"""
        return fake.address()


class RandomCompany():
    '''-------公司信息类--------'''

    def rc_company(self):
        """随机公司名"""
        return fake.company()

    def rc_company_suffix(self):
        """随机公司名后缀(公司性质)，比如网络有限公司"""
        return fake.company_suffix()

    def rc_company_prefix(self):
        """随机公司名前缀"""
        return fake.company_prefix()


class RandomDate():
    '''----------日期类----------'''

    def rdate_date(self):
        """随机格式化：年-月-日"""
        return fake.date(pattern="%Y-%m-%d", end_datetime=None)

    def rdate_year(self):
        """随机年份"""
        return fake.year()

    def rdate_day_of_week(self):
        """随机星期数"""
        return fake.day_of_week()

    def rdate_time(self):
        """随机时间"""
        return fake.time(pattern="%H:%M:%S", end_datetime=None)


class RandomWord():
    '''-----------文章类----------'''

    def rw_text(self):
        """随机生成一篇文章"""
        return fake.text()

    def rw_word(self, word_list=None):
        """随机词语   word_list可以是一个列表，那么词语会从列表中取"""
        return fake.word(ext_word_list=word_list)

    def rw_words(self, nb=3, word_list=None):
        """随机多个词语 nb是数量，对于words来说是返回多少个词语"""
        return fake.words(nb=nb, ext_word_list=word_list)

    def rw_sentence(self, nb=6, word_list=None):
        """随机短语（会包括短语结束标志点号）"""
        return fake.sentence(nb_words=nb, variable_nb_words=True, ext_word_list=word_list)

    def rw_paragraph(self, nb=3, word_list=None):
        """随机段落"""
        return fake.paragraph(nb_sentences=nb, variable_nb_sentences=True, ext_word_list=word_list)

    def rw_paragraphs(self, nb=3, word_list=None):
        """多个随机段落"""
        return fake.paragraphs(nb=nb, ext_word_list=word_list)


if __name__ == '__main__':
    person = RandomData()
    print(person.rd_int())
    # print(random_name())
    # print(random_address())
    # print(random_email())
