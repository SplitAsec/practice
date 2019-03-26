#퇴근시간계산기
import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap


class LeaveTimeApp(QWidget):
	
	
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
	def timeCal(self):                       #시간 계산
		cur_time = datetime.datetime.today()
		try:
			Comein_time = cur.time.replace(hour=Cinputhour, minute=Cinputminute, second=0)
			leave_time = cur_time.replace(hour=Linputhour, minute=Linputminuite, second=0)
		except:
			pass
		diffsec = (leave_time - cur_time)

	def initUI(self):
		Ctimebtn = QPushButton('출근 시간',self)    #출퇴근 시간 버튼 생성
		Ctimebtn.clicked.cnnect(self.Ctimeinput)
		Ltimebtn = QPushbutton('퇴근 시간',self)
		Ltimebtn.clicked.cnnect(self.Ltimeinput)
		
		try:
			CtimeDisplay = QLabel(f'출근시간 : {text1}')  #입력된 출퇴근 시간 출력
		except:
			CtimeDisplay = QLabel('출근시간 :')
		
		try:
			LtimeDisplay = QLabel(f'퇴근시간 : {text2}')
		except:
			CtimeDisplay = QLabel('퇴근시간 :')
			
		
		hbox = QHBoxLayOut()                           #버튼 정렬
		hbox.addSTretch(1)
		hbox.addWidget(Ctimebtn)
		hbox.addWidget(Ltimebtn)
		hbox.addStretch(1)
		
		vbox = QVBoxLayout()                           #버튼상자 및 시간 출력
		vbox.addStretch(3)
		vbox.addWidget(CtimeDisplay)
		vbox.addWidget(LtimeDisplay)
		vbox.addLayout(hbox)
		vbox.addStretch(1)
		
		self.setWindowTitle('퇴근 시간 계산기')            #윈도우 생성
		self.setWindowIcon(QIcon('clock.png'))
		self.move(300, 300)
		self.resize(400, 200)
		self.show()
	
	def Ctimeinput(self): #출근 시간 입력 다이얼로그창
		text1, ok1 = QinputDialog.getText(self, '출근 시간', 'OO시 OO분')
		if ok1:
			Cinputhour = int(text1[:1])
			Cinputminute = int(text1[4:5])

	def Ltimeinput(self): #퇴근 시간 입력 다이얼로그창
		text2, ok2 = QinputDialog.getText(self, '퇴근 시간', 'OO시 OO분')
		if ok2:
			Linputhour = int(text2[:1])
			Linputminuite = int(text2[4:5])