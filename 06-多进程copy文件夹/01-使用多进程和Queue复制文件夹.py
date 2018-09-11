from multiprocessing import Pool, Manager
import os

def copyFileTask(name, oldFolderName,newFolderName, queue):
	fr = open(oldFolderName + "/" + name)
	fw = open(newFolderName + "/" + name, "w+")#写方式
	#大文件的话需要一行一行读，这里是demo所以就直接读了
	content = fr.read()
	fw.write(content)
	fr.close()
	fw.close()
	print("--%s--copy-finished---"%name)
	queue.put(name)

def main():
	#1.获取要复制的文件夹名称
	oldFolderName = input("请输入要复制的文件夹的名称：")
	#读取文件，可能文件夹不存在，会抛出异常，所以先做判断
	try:
		#2.获取old文件列表
		oldFolderFiles = os.listdir(oldFolderName)
		print(oldFolderFiles)
		#3.创建一个新的文件夹
		newFolderName = oldFolderName + "-copy"
		try:
			os.mkdir(newFolderName)
		except Exception as exp:
			print(exp)
		
		#4.判断old文件夹中是否有文件，没有则不用复制
		if len(oldFolderFiles):
			'''文件夹中的文件数目大于0才需要复制'''
			#5.使用多进程进行文件夹复制
			pool = Pool(5)#创建进程池
			queue = Manager().Queue()#创建消息队列
			for name in oldFolderFiles:
				pool.apply_async(copyFileTask,(name, oldFolderName, newFolderName, queue))
		
			totalFileNum = len(oldFolderFiles)
			num = 0
			print("before getting")
			while num < totalFileNum:
				queue.get()
				num = num + 1
				copyRate = num / totalFileNum
				print("\rcopy的进度是:%.2f%%"%(copyRate*100))
			print("已经完成拷贝")
		
	except Exception as ret:
		print(ret)

if __name__ == "__main__":
	main()
