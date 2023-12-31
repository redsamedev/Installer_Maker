import os
import time
import webbrowser
print('Installer Maker Version 1.0')
"""
    the Script
    by GigaCoder
"""
#Welcome to Installer Maker main script
#Help List Variable
hlist = ['mk-installer: Make the Installer', 'ver: APP Version']
#APP Code
def app_main():
    #Languages Selection Variables
    english = True
    French = False
    Espagnole = False
    #Directory Source Variable
    Dir_Source = 'Example'
    #Application Info
    inf_app = ''
    for i in hlist:
        print('----------------------')
        print(i)
        print('----------------------')
    while True:
        #Command Selector Input
        cmd = input('Type_Command: ')
        if cmd == 'mk-installer':
            print('Select Languages:' + '\n' + '\n')
            #English Selector input
            Eng = input('English Language (is on by default) on/off: ')
            #French Selector Input
            Fra = input('French Language on/off: ')
            #Espagnole Selector Input
            esp = input('Espagnole Language on/off: ')
            print('\n' + '\n' + 'Select Directory Source')
            #Directory Source Selector Input
            dir_select = input('Select Directory Source: ')
            #Application or any file Info
            app_inf_select = input('File Info: ')
            #Logic
            if Eng == 'on' and Fra == 'off' and esp == 'off':
                english = True
                French = False
                Espagnole = False
            elif Eng == 'on' and Fra == 'on' and esp == 'on':
                english = True
                French = True
                Espagnole = True
            elif Eng == 'off' and Fra == 'on' and esp == 'off':
                english = False
                French = True
                Espagnole = False
            elif Eng == 'off' and Fra == 'off' and esp == 'on':
                english = False
                French = False
                Espagnole = True
            inf_app = app_inf_select
            Dir_Source = dir_select
            with open('settings.py', 'w') as settings_file:
                settings_file.write('english = ' + str(english) + '\n')
                settings_file.write('French = ' + str(French) + '\n')
                settings_file.write('Espagnole = ' + str(Espagnole) + '\n')
                settings_file.write('inf_app = "' + str(inf_app)+ '"' + '\n')
                settings_file.write('Dir_Source = "' + str(Dir_Source)+ '"' + '\n')
            with open('script.py', "w") as script_file, open('main_script', "r") as main_script:
                py_script = main_script.read()
                script_file.write(str(py_script))
                script_file.close()
            try:
                print('Converting the script to EXE file...')
                time.sleep(1.25)
                os.system('pip install pyinstaller')
                os.system(f'pyinstaller script.py --onefile --add-data "settings.py:." --name {inf_app}')
                time.sleep(1.25)
                print('the script converted to an exe file succesfully..')
                time.sleep(0.75)
            except:
                print('Somthing went wrong...')
            try:
                print('Removing the junk files...')
                time.sleep(0.75)
                os.remove('settings.py')
                os.remove('script.py')
                os.remove(f'{inf_app}.spec')
            except:
                print('Somthing went wrong!...')
            time.sleep(1.25)
            print('\nDone!')
            input('\npress enter to exit...')
            break
        elif cmd == 'ver':
            print('---------------------------' + '\n')
            print('Installer Maker Version 1.0' + '\n' + '\n' +'Application by GigaCoder' + '\n')
            print('---------------------------' + '\n')
            cc = input('do you want check my channel :) (y/n) : ')
            if cc == 'y':
                webbrowser.open('https://youtube.com/@gigacoder_')
            else:
                pass



if __name__ == '__main__':
    app_main()
