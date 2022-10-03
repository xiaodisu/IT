import os

class calculate():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def plus(self):
        res = f'两数之和为：{self.x} + {self.y} = {self.x + self.y}\n'
        print(res)
        return res
        
    def minus(self):
        res = f'两数之差为：{self.x} - {self.y} = {self.x - self.y}\n'
        print(res)
        return res
        
    def multiply(self):
        res = f'两数之积为：{self.x} * {self.y} = {self.x * self.y}\n'
        print(res)
        return res
        
    def divide(self):
        res = f'两数之商为：{self.x} / {self.y} = {self.x / self.y}\n'
        print(res)
        return res
    
    def mod(self):
        res = f'取模运算为：{self.x} % {self.y} = {self.x % self.y}\n'
        print(res)
        return res
        
    def all_(self):
        return self.plus(), self.plus(), self.multiply(), self.divide(), self.mod()
        

# 用户键盘输入
def keyboard():
    while True:
        try:
            x = eval(input('请输入第一个数x：'))
            if isinstance(x, int) or isinstance(x, float):
                break
            else:
                print('输入有误，请重新输入')
        except:
            print('输入有误，请重新输入')

    while True:
        try:
            y = eval(input('请输入第二个数y：'))
            if isinstance(y, int) or isinstance(y, float):
                break
            else:
                print('输入有误，请重新输入')
        except:
            print('输入有误，请重新输入')
    calculator = calculate(x, y)
    print(f'\nx = {x}, y ={y} 时计算结果如下：\n')
    res = calculator.all_()

# 文件导入
def file(path):
    data_lis = open(path).read().split('\n')
    output_data = []
    for data in data_lis:
        x, y = map(int, data.split(','))
        calculator = calculate(x, y)
        print(f'\nx = {x}, y ={y} 时计算结果如下：\n')
        res = calculator.all_()
        output_data.append(f'\nx = {x}, y ={y} 时计算结果如下：\n' + ''.join(res))
    output_yn = input('是否需要导出结果（y/n）')
    if output_yn == 'y':
        output_path = input('文件导出路径为：')
        open(output_path, 'a').write(output_data)
        
# 执行
def output():
    input_way = eval(input('您输入数据的方式为：（1：键盘输入，2：文件导入）'))
    if input_way == 1:
        while True:
            keyboard()
            continue_ = input('是否继续输入（y/n）')
            if continue_ == 'n':
                break
            if continue_ != 'n' and continue_ != 'y':
                print('请按要求输入')
    elif input_way == 2:
        try:
            path = input('请输入待处理文件路径：')
            if os.path.exists(path):
                file(path)
            else:
                print('您输入的待处理文件不存在')
                
        except:
            print('您的文件内容格式错误')
    
    else:
        print('您输入数据的方式错误')

output()
