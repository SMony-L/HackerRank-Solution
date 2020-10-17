import textwrap
def wrap(string,width):
    return ''.join(textwrap.fill(string,width))
    
if __name__ == '__main__':
    string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
    width = 4
    
    result = wrap(string,width)
    print(result)