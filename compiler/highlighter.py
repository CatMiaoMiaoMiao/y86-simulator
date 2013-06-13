'''
Python Syntax Highlighting Example

Copyright (C) 2009 Carson J. Q. Farmer

This program is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public Licence as published by the Free Software
Foundation; either version 2 of the Licence, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.	See the GNU General Public Licence for more 
details.

You should have received a copy of the GNU General Public Licence along with
this program; if not, write to the Free Software Foundation, Inc., 51 Franklin
Street, Fifth Floor, Boston, MA	02110-1301, USA
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MyHighlighter1( QSyntaxHighlighter ):

		def __init__( self, parent, theme ):
			QSyntaxHighlighter.__init__( self, parent )
			self.parent = parent
			instruction = QTextCharFormat()
			register = QTextCharFormat()
			immediate_hex = QTextCharFormat()
			immediate_dec = QTextCharFormat()
			memory = QTextCharFormat()
			number = QTextCharFormat()
			comment = QTextCharFormat()

			self.highlightingRules = []

			# instruction
			brush = QBrush( Qt.darkBlue, Qt.SolidPattern )
			instruction.setForeground( brush )
			instruction.setFontWeight( QFont.Bold )
			keywords = QStringList( [ "addl", "subl", "andl", "xorl", "jmp", "jle", "jl", "je", "jne", "jge", "jg",
									  "rrmovl", "irmovl", "rmmovl", "mrmovl", "pushl", "popl", "call", "ret", "halt",
                                      "isubl", "leave", "iaddl"] )
			for word in keywords:
				pattern = QRegExp("\\b" + word + "\\b")
				rule = HighlightingRule( pattern, instruction )
				self.highlightingRules.append( rule )



			# register
			brush = QBrush( Qt.darkYellow, Qt.SolidPattern )
			register.setForeground( brush )
			register.setFontWeight( QFont.Bold )
			keywords = QStringList( [ "%eax", "%ecx", "%edx", "%ebx", "%esp", "%ebp", "%esi", "%edi"] )
			for word in keywords:
				pattern = QRegExp(word)
				rule = HighlightingRule( pattern, register )
				self.highlightingRules.append( rule )

			#memory
			brush = QBrush( Qt.blue, Qt.SolidPattern )
			memory.setFontWeight( QFont.Bold )
			pattern = QRegExp( "[\)\(]+")
			pattern.setMinimal( False )
			memory.setForeground( brush )
			rule = HighlightingRule( pattern, memory )
			self.highlightingRules.append( rule )



			# immediate_hex
			brush = QBrush( Qt.magenta, Qt.SolidPattern )
			immediate_hex.setForeground( brush )
			immediate_hex.setFontWeight( QFont.Bold )
			pattern = QRegExp( "\$0x[0-9a-f]+")
			pattern.setMinimal( False )
			number.setForeground( brush )
			rule = HighlightingRule( pattern, number )
			self.highlightingRules.append( rule )
			
			# immediate_dec
			brush = QBrush( Qt.darkMagenta, Qt.SolidPattern )
			immediate_dec.setForeground( brush )
			immediate_dec.setFontWeight( QFont.Bold )
			pattern = QRegExp( "\$[0-9]+")
			pattern.setMinimal( False )
			number.setForeground( brush )
			rule = HighlightingRule( pattern, number )
			self.highlightingRules.append( rule )

			# comment
			brush = QBrush( Qt.gray, Qt.SolidPattern )
			pattern = QRegExp( "#[^\n]*" )
			comment.setForeground( brush )
			rule = HighlightingRule( pattern, comment )
			self.highlightingRules.append( rule )


		def highlightBlock( self, text ):
			for rule in self.highlightingRules:
				expression = QRegExp( rule.pattern )
				index = expression.indexIn( text )
				while index >= 0:
					length = expression.matchedLength()
					self.setFormat( index, length, rule.format )
					index = text.indexOf( expression, index + length )
			self.setCurrentBlockState( 0 )

class HighlightingRule():
	def __init__( self, pattern, format ):
		self.pattern = pattern
		self.format = format
		
class TestApp( QMainWindow ):
	def __init__(self):
		QMainWindow.__init__(self)
		editor = QTextEdit()
		highlighter = MyHighlighter( editor, "Classic" )
		self.setCentralWidget( editor )
		self.setWindowTitle( "Syntax Highlighter" )
		

