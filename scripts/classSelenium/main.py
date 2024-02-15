from logicTree.store_selenium import Store_Selenium

with Store_Selenium() as bot:

    bot.get_url()
    bot.fill_form()