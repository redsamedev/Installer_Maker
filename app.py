print('Installer Maker Version 1.0')
"""
    the Script
    by GigaCoder
"""
#Welcome to Installer Maker main script

#Languages Selection Variables
english = True
French = False
Espagnole = False
#Directory Source Variable
Dir_Source = 'Example'
#Application Info
inf_app = ''
#Help List Variable
hlist = ['mk-installer: Make the Installer', 'ver: APP Version']
#APP Code
def app_main():
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
            with open('script.py', 'w') as script_file:
                script_file.write('')
        elif cmd == 'ver':
            print('---------------------------' + '\n')
            print('Installer Maker Version 1.0' + '\n' + '\n' +'Application by GigaCoder' + '\n')
            print('---------------------------' + '\n')

if __name__ == '__main__':
    app_main()