"""
将阿拉伯数字转为中文大写
精确到小数点后两位
数字最大至亿级别
"""
import argparse

parse= argparse.ArgumentParser()
parse.add_argument('--input', type=float, default=0, help='输入大于零小于十亿，最多精确到小数点后两位的阿拉伯数字，')
args=parse.parse_args()

number_man_dic={
                0:'零', 1:'壹', 2:'贰', 3:'叁', 4:'肆',
                5:'伍', 6:'陆', 7:'柒', 8:'捌', 9:'玖', 10:'拾',
                '百':'佰', '千':'仟', '万':'万',          
                }

def num2man(inputNumber):
    #1.检查数字范围，非负数，不符则重新输入
    if inputNumber<=0 or inputNumber>999999999 :
        print('输入数字不符要求，请重新输入。请保证是阿拉伯数字，应小于十亿且为非负数。')
        assert inputNumber>0 and inputNumber<=999999999, "Wrong Number Form"
    #2.分解数字
    hundred_million=inputNumber//100000000%10#亿
    ten_million=inputNumber//10000000%10#千万
    million=inputNumber//1000000%10#百万
    hundred_thousand=inputNumber//100000%10#十万
    ten_thousand=inputNumber//10000%10#万
    thousand=inputNumber//1000%10#千
    hundred=inputNumber//100%10#百
    ten=inputNumber//10%10#十
    unit=inputNumber//1%10#个
    decile=inputNumber%1*100//10%10#十分
    percentile=inputNumber%1*100//1%10#百分
    
    
    # print('your input is {inp}'.format(inp=inputNumber))
    # print(hundred_million, ten_million, million)
    # print(hundred_thousand, ten_thousand)
    # print(thousand, hundred, ten, unit)
    # print(decile, percentile)
    #3.返回结果
    result=''

    if hundred_million!=0:#亿
        result+=number_man_dic[hundred_million]+'亿'

    if ten_million!=0:#千万
        result+=number_man_dic[ten_million]+number_man_dic['千']
    elif ten_million==0 and inputNumber>=100000000 and hundred_million!=0:
        result+=number_man_dic[0]

    if million!=0:#百万
        result+=number_man_dic[million]+number_man_dic['百']
    elif million==0 and inputNumber>=1000000 and ten_million!=0: result+=number_man_dic[0]#千万位为0且本位为0
    

    if hundred_thousand!=0:#十万
        result+=number_man_dic[hundred_thousand]+number_man_dic[10]
    elif hundred_thousand==0 and inputNumber>=100000 and million!=0 and ten_thousand!=0: result+=number_man_dic[0]

    if ten_thousand!=0:#万
        result+=number_man_dic[ten_thousand]+number_man_dic['万']
    elif ten_thousand==0 and inputNumber>=10000:
        result+=number_man_dic['万']

    if thousand!=0:#千
        result+=number_man_dic[thousand]+number_man_dic['千']
    elif thousand==0 and inputNumber>=1000 and hundred!=0: result+=number_man_dic[0]
       

    if hundred!=0:#百
        result+=number_man_dic[hundred]+number_man_dic['百']
    elif hundred==0 and inputNumber>=100 and ten!=0: result+=number_man_dic[0]

    if ten!=0:#十
        result+=number_man_dic[ten]+number_man_dic[10]
    elif ten==0 and inputNumber>=10 and unit!=0: result+=number_man_dic[0]

    if unit!=0:#个
        result+=number_man_dic[unit]+'元'
    elif unit==0:
        result+='元'

    if decile==0 and percentile==0:
        result+='整'
        return result

    if decile!=0:
        result+=number_man_dic[decile]+'角'
        if percentile!=0:
            result+=number_man_dic[percentile]+'分'
    elif decile==0 and percentile!=0:
        result+=number_man_dic[0]+ number_man_dic[percentile]+'分'
    return result



if __name__=="__main__":
    k=args.input
    #k=0
    p=num2man(k)
    print(p)
    