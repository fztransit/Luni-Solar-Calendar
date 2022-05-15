from CustomizeWidgets import *
from PerpetualCalendar import *

class GUI(QMainWindow):
	def __init__(self):
		super().__init__()
		self.wnlWidget = QWidget()
		self.setupUI()

	def setupUI(self):
		pe = QPalette()
		pe.setColor(QPalette.Window, QColor(250, 255, 255))  # F0FFFF、FFFAFA、FFFAF0
		self.setPalette(pe)
		self.setFixedSize(470, 380)
		self.setWindowTitle("万年历")
		self.setCentralWidget(self.wnlWidget)
		self.calendarUI()

		displayDate(self)
		self.show()

	def calendarUI(self):
		self.gridWNL = QGridLayout()
		self.wnlWidget.setLayout(self.gridWNL)
		self.gridWNL.setSpacing(0)
		self.hlayWNL = QHBoxLayout()
		self.hlayWNL.setContentsMargins(3, 0, 5, 0)
		self.gridWNL.addLayout(self.hlayWNL, 0, 0, 1, 7)
		self.cblCentury = ComboBox()
		for i in range(startCentury, endCentury+1):
			if i < 0: self.cblCentury.addItem('BC' + str(abs(i)) + '世纪')
			elif i == 0: continue
			else: self.cblCentury.addItem(str(i) + '世纪')
		self.cblCentury.currentIndexChanged.connect(lambda : yearItems(self))
		self.cblCentury.activated.connect(lambda : displayDate(self))
		self.cblCentury.setMaximumWidth(80)
		self.cblCentury.setFocusPolicy(False)
		self.hlayWNL.addWidget(self.cblCentury)
		self.cblYear = ComboBox()
		self.cblYear.setFixedWidth(82)
		self.btnLastYear = QPushButton('<')
		self.btnNextYear = QPushButton('>')
		self.cblYear.activated.connect(lambda : displayDate(self))
		self.cblYear.wheeled.connect(lambda :jumpYear(self))
		self.btnLastYear.clicked.connect(self.thisJumpMonth)
		self.btnNextYear.clicked.connect(self.thisJumpMonth)
		self.btnLastYear.setMaximumSize(16, 22)
		self.btnNextYear.setMaximumSize(16, 22)
		self.hlayWNL.addStretch()
		self.hlayWNL.addWidget(self.btnLastYear)
		self.hlayWNL.addWidget(self.cblYear)
		self.hlayWNL.addWidget(self.btnNextYear)
		self.cblMonth = ComboBox()
		for i in range(12):
			self.cblMonth.addItem(str(i + 1) + '月')
		self.cblMonth.setMaxVisibleItems(12)
		self.cblMonth.setFocusPolicy(False)
		self.cblMonth.setMaximumWidth(60)
		self.btnLastMonth = QPushButton("<")
		self.btnNextMonth = QPushButton(">")
		self.cblMonth.activated.connect(lambda : displayDate(self))
		self.cblMonth.wheeled.connect(lambda :jumpMonth(self))
		self.btnLastMonth.clicked.connect(self.thisJumpMonth)
		self.btnNextMonth.clicked.connect(self.thisJumpMonth)
		self.btnLastMonth.setMaximumSize(16, 22)
		self.btnNextMonth.setMaximumSize(16, 22)
		self.hlayWNL.addStretch()
		self.hlayWNL.addWidget(self.btnLastMonth)
		self.hlayWNL.addWidget(self.cblMonth)
		self.hlayWNL.addWidget(self.btnNextMonth)
		self.hlayWNL.addStretch()
		self.btnToday = QPushButton("今日")
		self.btnToday.clicked.connect(lambda : displayDate(self))
		self.btnToday.setMaximumWidth(36)
		self.hlayWNL.addWidget(self.btnToday)
		self.labMonday = Label("一")
		self.labTuesday = Label("二")
		self.labWednesday = Label("三")
		self.labThursday = Label("四")
		self.labFriday = Label("五")
		self.labSaturday = Label("六")
		self.labSunday = Label("日")
		labWeeks = [self.labMonday, self.labTuesday, self.labWednesday, self.labThursday, self.labFriday, self.labSaturday, self.labSunday]
		for i in range(7):
			self.gridWNL.addWidget(labWeeks[i], 1, i)
			labWeeks[i].setMaximumHeight(40)
		self.labs = []  # 6行7列日期标签
		for i in range(6):
			for j in range(7):
				if j == 0: self.labs.append([Label()])
				else: self.labs[i].append(Label())
				self.labs[i][j].setFixedSize(48, 48)
				self.labs[i][j].clicked.connect(lambda : displayDate(self))
				self.gridWNL.addWidget(self.labs[i][j], i + 2, j)
		self.cblFindFestival = QComboBox()
		self.cblFindFestival.addItem('查找农历节日')
		for festival in lcfestivals:
			self.cblFindFestival.addItem(festival[-1])
		self.cblFindFestival.activated.connect(self.thisJumpFestival)
		self.cblFindFestival.setStyleSheet("QComboBox { leftPadding: 1px }")
		self.cblFindFestival.setMaximumWidth(100)
		self.hlayGL = QHBoxLayout()
		self.hlayGL.addWidget(self.cblFindFestival)
		self.labInfo = QLabel()
		self.labInfo.setStyleSheet("QLabel{ font:14px;}")
		self.labInfo.setAlignment(Qt.AlignHCenter)
		self.labInfo.setContentsMargins(0, 6, 5, 6)
		self.labInfo.setWordWrap(True)
		self.labInfo.setFixedWidth(120)
		self.gridWNL.addLayout(self.hlayGL, 0, 7, 1, 1)
		self.gridWNL.addWidget(self.labInfo, 1, 7, 7, 1)

	def thisJumpMonth(self):
		if self.sender() == self.btnLastMonth:
			lastMonth(self)
		elif self.sender() == self.btnNextMonth:
			nextMonth(self)
		elif self.sender() == self.btnLastYear:
			lastYear(self)
		elif self.sender() == self.btnNextYear:
			nextYear(self)
		displayDate(self)

	def thisJumpFestival(self):
		if self.cblFindFestival.currentText() != '查找农历节日':
			displayDate(self)