print('see you Japan ')

# 飛行機中作業（遊び）
# Do you ride the fright
def fright():
    while True:
        print('do you wanaa ride this fright?')
        answer = input('select Yes or No')
        if answer == 'Yes':
            print('have a Nice day')
            break

        else:
            print('Why do you think so?')
            add_answer = input('why?')
            

fright()