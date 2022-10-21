from core.data import read_excel
from core.AppiumAction import AppiumKeyWords


def test_demo():
    # declare testing Configs
    # Android Device
    desire_caps = {
        'platformName': 'Android',
        'platformVersion': '10',
        'deviceName': 'xxx',
        'appPackage': 'hko.MyObservatory_v1_0',
        'appActivity': 'hko.MyObservatory_v1_0.AgreementPage',
        'unicodeKeyBoard': True,
        'resetKeyboard': True,
        'noReset': True,
        'newCommandTimeout': 6000,
        'automationName': 'UiAutomator2'
    }
    # initialize Keyword driven
    kw = AppiumKeyWords(desire_caps)

    # load 1 Excel file(only 1 active sheet so far) by row
    for row in read_excel("caseFile/test_ui.xlsx"):
        id = row[0]
        # only valid id are steps
        if isinstance(id,int) and id >0:
            # keyword in column 2
            oper = row[2]
            # reflects keyword function
            func = getattr(kw, str(oper))
            # remove None for param
            params = [i for i in row[3:] if i]
            # temp resolve for click func with ele and eles
            if oper == "click" and row[5] is None:
                params.append(None)
            # call keyword func
            func(*params)
