import os
card_infos = []

def print_menu():
    """打印菜单列表"""
    print("="*50)
    print("名片管理系统")
    print(" 1. 添加一个新名片")
    print(" 2. 删除一个名片")
    print(" 3. 修改一个名片")
    print(" 4. 查询一个名片")
    print(" 5. 显示所有名片")
    print(" 6. 将信息保存到文件中")
    print(" 7. 退出系统")
    print("=" * 50)
def load_data():
    """从文件中加载数据"""
    f = None
    global card_infos
    try:
        f = open("card.data","r")
        card_infos = eval(f.read())
    except Exception:
        pass
    finally:
        if f:
            f.close()
def save_2_file():
    """将数据保存在文件中"""
    f = None
    global card_infos
    try:
        f = open("card.data", "w")
        f.write(str(card_infos))
    except Exception:
        pass
    finally:
        if f:
            f.close()
def add_new_card_info():
    """添加一张卡片"""
    new_name = input("请输入新的名字：")
    new_qq = input("请输入新的QQ：")
    new_weixin = input("请输入新的微信：")
    new_addr = input("请输入新的住址：")

    new_info = dict()
    new_info["name"] = new_name
    new_info["qq"] = new_qq
    new_info["weixin"] = new_weixin
    new_info["addr"] = new_addr

    global card_infos
    card_infos.append(new_info)
    print("添加卡片成功！")
def delete_card():
    name = input("请输入要删除的名字")
    del_card = {}
    global card_infos
    for card in card_infos:
        if card["name"] == name:
            del_card = card
            break
    if del_card:
        card_infos.remove(del_card)
        return True
    else:
        return False
def modify_card():
    name = input("请输入卡片的名称：")
    old_card ={}
    global  card_infos
    for card in card_infos:
        if card["name"] == name:
            old_card = card
            break
    if old_card:
        old_card["qq"] = input("请输入新的QQ：")
        old_card["weixin"] = input("请输入新的微信：")
        old_card["addr"] = input("请输入新的住址：")
        return True
    return False
def query_card():
    name = input("请输入要查找的名称：")
    global card_infos
    for card in card_infos:
        if card["name"] == name:
            print("%s\t%s\t%s\t%s"%(card["name"],card["qq"],card["weixin"],card["addr"]))
            True
    return False
def query_all():
    global card_infos
    print("姓名\tQQ\t微信\t住址")
    for card in card_infos:
        print("%s\t%s\t%s\t%s" % (card["name"], card["qq"], card["weixin"], card["addr"]))
def main():
    #从文件中加载数据
    load_data()
    #打印菜单列表
    print_menu()
    while True:
        code = int(input("请输入操作编码:"))

        if code == 1:
            add_new_card_info()
        elif code == 2:
            result = delete_card()
            if result:
                print("删除成功")
            else:
                print("删除失败")
        elif code == 3:
            result = modify_card()
            if result:
                print("修改成功")
            else:
                print("修改失败,改卡片不存在！")
        elif code == 4:
            result = query_card()
            if not result:
                print("卡片不存在")
        elif code == 5:
            query_all()
        elif code == 6:
            save_2_file()
        elif code == 7:
            break
        else:
            print("请输入正确的编号！")
        print("")

main()

