from aiogram import types

#Back to ...
BackToMenu = types.InlineKeyboardButton('Перейти в меню', callback_data='menu')
BackToSettings = types.InlineKeyboardButton('Перейти в настройки', callback_data='settings')
BackToAlert = types.InlineKeyboardButton('Перейти в уведомления', callback_data='alert open')

#MainMenu
MainMenu = types.InlineKeyboardMarkup()
Alert = types.InlineKeyboardButton('Всякий раз, когда ниже определенной стоимости', callback_data='alert value')
MainMenu.add(Alert)
Settings = types.InlineKeyboardButton('Всякий раз, когда появляется монета с наименьшей стоимостью', callback_data='alert min')
MainMenu.add(Settings)

#Alert
Alert = types.InlineKeyboardMarkup()
addAlert = types.InlineKeyboardButton('Добавить новое уведомление', callback_data='alert add')
Alert.add(addAlert)
showAlerts = types.InlineKeyboardButton('Посмотреть свои уведомления', callback_data='alert show')
Alert.add(showAlerts)
deleteAlerts = types.InlineKeyboardButton('Удалить все свои уведомления', callback_data='alert delete')
Alert.add(deleteAlerts)
HelpAlert = types.InlineKeyboardButton('Помощь', callback_data='alert help')
Alert.add(HelpAlert)
Alert.add(BackToMenu)

def AddAlertExtended(OpenedCurrency):
    AddAlertMarkup = types.InlineKeyboardMarkup()

    for Currency in OpenedCurrency:
            AddAlertMarkup.add(types.InlineKeyboardButton(f'{Currency}',
                                                          switch_inline_query_current_chat=f'{Currency} измениттся на 10%'
                                                                                           f'за последние 2 часа'))

    AddAlertMarkup.add(BackToAlert)

    AddAlertMarkup.add(BackToMenu)

    return AddAlert

#AddAlerts
def AddAlert(OpenedCurrency):
    AddAlertMarkup = types.InlineKeyboardMarkup()

    for Currency in OpenedCurrency:
            AddAlertMarkup.add(types.InlineKeyboardButton(f'{Currency}', callback_data=f'alert {Currency}'))

    AddAlertMarkup.add(BackToAlert)

    AddAlertMarkup.add(BackToMenu)

    return AddAlertMarkup

def CurrencyJump(Currency):
    CurrencyJumpMarkup = types.InlineKeyboardMarkup()
    CurrencyJumpMarkup.add(types.InlineKeyboardButton(f'{Currency} изменится на 5%', callback_data= f'alert {Currency} 5%'))
    CurrencyJumpMarkup.add(types.InlineKeyboardButton(f'{Currency} изменится на 10%', callback_data= f'alert {Currency} 10%'))
    CurrencyJumpMarkup.add(types.InlineKeyboardButton(f'{Currency} изменится на 20%', callback_data= f'alert {Currency} 20%'))
    CurrencyJumpMarkup.add(types.InlineKeyboardButton(f'{Currency} изменится на 50%', callback_data= f'alert {Currency} 50%'))
    CurrencyJumpMarkup.add(types.InlineKeyboardButton(f'{Currency} изменится на 100%', callback_data= f'alert {Currency} 100%'))

    CurrencyJumpMarkup.add(BackToAlert)

    CurrencyJumpMarkup.add(BackToMenu)

    return CurrencyJumpMarkup

def AlertTime(Currency, jump):
    AlertTimeMarkup = types.InlineKeyboardMarkup()
    AlertTimeMarkup.add(types.InlineKeyboardButton(f'{Currency} изменится на {jump}% за последний час',
                                                   callback_data= f'alert {Currency} {jump} 1 time'))
    AlertTimeMarkup.add(types.InlineKeyboardButton(f'{Currency} изменится на {jump}% за последние 2 часа',
                                                   callback_data= f'alert {Currency} {jump} 2 time'))
    AlertTimeMarkup.add(types.InlineKeyboardButton(f'{Currency} изменится на {jump}% за последних 5 часов',
                                                   callback_data= f'alert {Currency} {jump} 5 time'))
    AlertTimeMarkup.add(types.InlineKeyboardButton(f'{Currency} изменится на {jump}% за последних 12 часов',
                                                   callback_data= f'alert {Currency} {jump} 12 time'))
    AlertTimeMarkup.add(types.InlineKeyboardButton(f'{Currency} изменится на {jump}% за последние 24 часа',
                                                   callback_data= f'alert {Currency} {jump} 24 time'))

    AlertTimeMarkup.add(BackToAlert)

    AlertTimeMarkup.add(BackToMenu)

    return AlertTimeMarkup


def ShowAlerts(user_id, Alerts):
    AlertsKeyboard = types.InlineKeyboardMarkup()
    for alert in Alerts.values():
        if alert.user_id == user_id:
            AlertsKeyboard.add(types.InlineKeyboardButton(alert.text, callback_data= f'alert {alert.text_id}'))

    AlertsKeyboard.add(BackToAlert)

    AlertsKeyboard.add(BackToMenu)

    return AlertsKeyboard


#Settings
Settings = types.InlineKeyboardMarkup()
ownCurrency = types.InlineKeyboardButton('Родная валюта', callback_data='ownCurrency')
Settings.add(ownCurrency)
SelectCurrency = types.InlineKeyboardButton('Фильтр криптовалют', callback_data='SelectCurrency')
Settings.add(SelectCurrency)
Settings.add(BackToMenu)

def ShowSelectedCurrency(AllCurrencies, OpenedCurrencies):
    AllSelectedCurrenciesKeyboard = types.InlineKeyboardMarkup()

    for Currency in AllCurrencies:
        if OpenedCurrencies[Currency]:
            AllSelectedCurrenciesKeyboard.add(types.InlineKeyboardButton(f'{Currency} ✅', callback_data=f'{Currency}'))
        else:
            AllSelectedCurrenciesKeyboard.add(types.InlineKeyboardButton(f'{Currency}', callback_data=f'{Currency}'))

    AllSelectedCurrenciesKeyboard.add(types.InlineKeyboardButton('Отметить все', callback_data='reset true'))
    AllSelectedCurrenciesKeyboard.add(types.InlineKeyboardButton('Сбросить', callback_data='reset false'))

    AllSelectedCurrenciesKeyboard.add(BackToSettings)
    AllSelectedCurrenciesKeyboard.add(BackToMenu)

    return AllSelectedCurrenciesKeyboard

def OwnCurrencies(currency):
    OwnCurrenciesKeyboard = types.InlineKeyboardMarkup()

    if currency == 'USD':
        Currency_USD = types.InlineKeyboardButton('USD ✅', callback_data='USD')
    else:
        Currency_USD = types.InlineKeyboardButton('USD', callback_data='USD')
    if currency == 'UAH':
        Currency_UAH = types.InlineKeyboardButton('UAH ✅', callback_data='UAH')
    else:
        Currency_UAH = types.InlineKeyboardButton('UAH', callback_data='UAH')

    if currency == 'RUB':
        Currency_RUB = types.InlineKeyboardButton('RUB ✅', callback_data='RUB')
    else:
        Currency_RUB = types.InlineKeyboardButton('RUB', callback_data='RUB')

    OwnCurrenciesKeyboard.add(Currency_USD)

    OwnCurrenciesKeyboard.add(Currency_UAH)

    OwnCurrenciesKeyboard.add(Currency_RUB)

    OwnCurrenciesKeyboard.add(BackToSettings)
    OwnCurrenciesKeyboard.add(BackToMenu)

    return OwnCurrenciesKeyboard

#Registration
def OwnCurrencyReg():
    OwnCurrencyReg = types.InlineKeyboardMarkup()

    Currency_USD = types.InlineKeyboardButton('USD', callback_data='reg USD ownCurrency')
    Currency_UAH = types.InlineKeyboardButton('UAH', callback_data='reg UAH')
    Currency_RUB = types.InlineKeyboardButton('RUB', callback_data='reg RUB')

    OwnCurrencyReg.add(Currency_USD)

    OwnCurrencyReg.add(Currency_UAH)

    OwnCurrencyReg.add(Currency_RUB)

    return OwnCurrencyReg

def ShowSelectedCurrencyReg(AllCurrencies, OpenedCurrencies):
    AllSelectedCurrenciesKeyboardReg = types.InlineKeyboardMarkup()

    for Currency in AllCurrencies:
        if OpenedCurrencies[Currency]:
            AllSelectedCurrenciesKeyboardReg.add(types.InlineKeyboardButton(f'{Currency} ✅', callback_data=f'reg {Currency}'))
        else:
            AllSelectedCurrenciesKeyboardReg.add(types.InlineKeyboardButton(f'{Currency}', callback_data=f'reg {Currency}'))

    AllSelectedCurrenciesKeyboardReg.add(types.InlineKeyboardButton('Отметить все', callback_data='reg reset true'))
    AllSelectedCurrenciesKeyboardReg.add(types.InlineKeyboardButton('Сбросить', callback_data='reg reset false'))

    AllSelectedCurrenciesKeyboardReg.add(types.InlineKeyboardButton('Продожить регистрацию', callback_data='reg continue'))

    return AllSelectedCurrenciesKeyboardReg
