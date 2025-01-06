#file not found

try:
    file = open('a_text.txt')
    a_dic = {'key':'value'}
    print(a_dic['key2'])
    
except FileNotFoundError:
    #print('There was an error')
    file = open('a_text.txt', 'w')
    file.write('hello from francis')
    
except KeyError as error_msg:
    print(f'The key {error_msg} does not exist')
    
else:
    content = file.read()
    print(content)
    
    
finally:
    file.close()
    
    