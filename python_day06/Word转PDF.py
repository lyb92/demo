# import win32com
# import win32api
# import wmi
# import os, sys
# from docx import Document
# from win32com.client import constants, gencache
import os
# from xml.dom.minidom import Document

wdLine = 5
wdCollapseEnd = 0

try:
    import UiBot
except Exception as e:
    class Temp():
        def GetString(self, strPath):
            return ""


    UiBot = Temp()

__default_msg = {
    "WordToPDF": "word转换至PDF异常",
    "PDFToWord": "PDF转换至word异常"
}


def WordToPDF(path):
    pre_msg = __default_msg["WordToPDF"]
    temp = path.split('.')
    if temp[-1] != "docx" and temp[-1] != "doc":
        raise Exception("{0} - {1}".format(pre_msg, "传入的不是word文件"))
    if os.path.exists(path) is False:
        raise Exception("{0} - {1}".format(pre_msg, "文件不存在"))

    pdf_path = "".join(temp[:-1]) + ".pdf"
    word = gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(path, ReadOnly=1)
    doc.ExportAsFixedFormat(pdf_path, constants.wdExportFormatPDF)
    doc.Close(True, 0, False)
    doc = None
    # word.Quit(True, 0, False)
    # word = None
    return pdf_path


def delrow(filepath, tabindex, cellindex, keystr):
    """
    删除某个单元格内容为XX的行
    :param filepath:文件路径 注意转移符
    :param tabindex:一行的第几个单元格 从0 开始
    :param cellindex:一行的第几个单元格 从0 开始
    :param keystr:单元格的内容等于的关键字
    :return:
    """
    doc = Document(filepath)
    # 获取需要操作的范格
    tl = doc.tables[tabindex]
    #   获取表格的行
    rs = tl.rows
    for rr in rs:
        #  判断是否需要刚除该为这里使用一个示例喇断条件：如果第一个单元格的文字为"删刚除"，则删捌除该行
        if rr.cells[cellindex].text == keystr:
            # 涮除该行
            rr._element.getparent().remove(rr._element)
    #  保存馋后的wond义档
    doc.save(filepath)


def GetString(strpath):
    msg = UiBot.GetString(strpath)
    if not msg:
        msg = ""
    return msg


def MovePosition(doc, iMove, OptOrType="text", Position="right", Shift=False):
    prefix = GetString('Word/MovePositionExceptionPrefix')
    if not DocCheck(doc):
        raise Exception('{0}"Doc" {1}'.format(prefix, GetString('Word/ComTypeError')))

    if not (isinstance(iMove, int) or isinstance(iMove, str)):
        raise Exception('{0}"Count" {1}'.format(prefix, GetString('Word/InvalidValue')))
    if isinstance(iMove, str):
        succ, iMove = StrToInt(iMove)
        if not succ:
            raise Exception('{0}"Count" {1}'.format(prefix, iMove))
    if iMove < 0:
        raise Exception('{0}"Count" {1} 0'.format(prefix, GetString('Word/GreatOrEqual')))

    strType = 'text'
    strPosition = 'right'
    bShift = False
    if OptOrType:
        if isinstance(OptOrType, dict):
            if 'sType' in OptOrType:
                strType = OptOrType['sType']
            if 'sPosition' in OptOrType:
                strPosition = OptOrType['sPosition']
            if 'bShift' in OptOrType:
                bShift = OptOrType['bShift']
        else:
            strType = OptOrType
            strPosition = Position
            bShift = Shift

    if not isinstance(strType, str):
        raise Exception('{0}"Type" {1}'.format(prefix, GetString('Word/StringTypeError')))
    strType = strType.lower()
    if not (strType == 'text' or \
            strType == 'line' or \
            strType == 'section'):
        raise Exception('{0}"Type" {1}'.format(prefix, GetString('Word/InvalidValue')))

    if not isinstance(strPosition, str):
        raise Exception('{0}"Direction" {1}'.format(prefix, GetString('Word/StringTypeError')))
    strPosition = strPosition.lower()
    if not (strPosition == 'left' or \
            strPosition == 'right' or \
            strPosition == 'up' or \
            strPosition == 'down'):
        raise Exception('{0}"Direction" {1}'.format(prefix, GetString('Word/InvalidValue')))

    if iMove == 0:
        return

    try:
        win = None
        doc.Activate()
        try:
            win = doc.ActiveWindow
        except:
            pass
        if win:
            win.Activate()
            unit = None
            if strType == 'text':
                unit = wdCharacter
                if strPosition == 'up':
                    strPosition = 'left'
                elif strPosition == 'down':
                    strPosition = 'right'
                start = 0
                end = 0
                if strPosition == 'left':
                    # the selection is collapsed to the endpoint and moved to the left.
                    win.Selection.Collapse(wdCollapseStart)
                    end = win.Selection.Start
                    win.Selection.MoveLeft(unit, iMove)
                    start = win.Selection.Start
                elif strPosition == 'right':
                    # the selection is collapsed to the endpoint and moved to the right
                    win.Selection.Collapse(wdCollapseEnd)
                    start = win.Selection.End
                    win.Selection.MoveRight(unit, iMove)
                    end = win.Selection.End
                if bShift:
                    win.Selection.SetRange(start, end)
            elif strType == 'line' or strType == 'section':
                if strType == 'line':
                    unit = wdLine
                else:
                    unit = wdParagraph
                if strPosition == 'left':
                    strPosition = 'up'
                elif strPosition == 'right':
                    strPosition = 'down'
                start = 0
                end = 0
                if strPosition == 'up':
                    # the selection is collapsed to the endpoint and moved up.
                    win.Selection.Collapse(wdCollapseStart)
                    end = win.Selection.Start
                    win.Selection.MoveUp(unit, iMove)
                    start = win.Selection.Start
                elif strPosition == 'down':
                    # the selection is collapsed to the endpoint and moved down.
                    win.Selection.Collapse(wdCollapseEnd)
                    start = win.Selection.End
                    win.Selection.MoveDown(unit, iMove)
                    end = win.Selection.End
                if bShift:
                    win.Selection.SetRange(start, end)
    except Exception as e:
        raise Exception('{0}{1}'.format(prefix, e))


def DocCheck(doc):
    name = str(type(doc))
    pos = name.find('win32com.gen_py')
    if pos == -1:
        return False
    else:
        return True


def read_table(doc, table_index):
    if not DocCheck(doc):
        raise Exception('{0}"Doc" {1}'.format(prefix, GetString('Word/ComTypeError')))
    if doc.Tables.__len__() < table_index or table_index < 1:
        raise Exception("不存在第{0}张表格，请重新选择".format(table_index))
    table = doc.Tables(table_index)
    table_data = []
    for row in range(1, table.Rows.Count + 1):
        temp = []
        for col in range(1, table.Columns.Count + 1):
            try:
                data = table.Cell(row, col).Range.Text[:-2]
            except:
                data = ""
            temp.append(data)
        print(temp)
        table_data.append(temp)
    return table_data


def create_table(doc, row, col):
    prefix = "插入表格异常 "
    if not DocCheck(doc):
        raise Exception('{0}"Doc" {1}'.format(prefix, GetString('Word/ComTypeError')))

    if not (isinstance(row, int) and isinstance(row, int)):
        raise Exception('{0}"行/列" {1}'.format(prefix, GetString('Word/IntTypeError')))

    if row <= 0 or col <= 0:
        raise Exception('{0}"行/列" {1}1'.format(prefix, GetString('Word/GreatOrEqual')))
    try:
        win = None
        doc.Activate()
        try:
            win = doc.ActiveWindow
        except:
            pass
        if win:
            win.Activate()
            table = doc.Tables.Add(Range=win.Selection.Range, NumRows=row, NumColumns=col)
            table.Borders.InsideLineStyle = win32com.client.constants.wdLineStyleSingle
            table.Borders.OutsideLineStyle = win32com.client.constants.wdLineStyleSingle
            MovePosition(doc, row, OptOrType="line", Position="down", Shift=False)
    except Exception as e:
        raise Exception('{0}{1}'.format(prefix, e))


def write_table(doc, text, table_index, row, col):
    prefix = "写入表格异常 "
    if not DocCheck(doc):
        raise Exception('{0}"Doc" {1}'.format(prefix, GetString('Word/ComTypeError')))
    if doc.Tables.__len__() < table_index or table_index < 1:
        raise Exception("不存在第{0}张表格，请重新选择".format(table_index))
    if not isinstance(text, str):
        raise Exception('{0}"Text" {1}'.format(prefix, GetString('Word/StringTypeError')))
    if not (isinstance(row, int) and isinstance(row, int)):
        raise Exception('{0}"行/列" {1}'.format(prefix, GetString('Word/IntTypeError')))
    if row <= 0 or col <= 0:
        raise Exception('{0}"行/列" {1}1'.format(prefix, GetString('Word/GreatOrEqual')))

    table = doc.Tables(table_index)
    if row > table.Rows.Count or col > table.Columns.Count:
        raise Exception('{0}"行/列" {1} 超出表格最大行/列'.format(prefix, GetString('Word/InvalidValue')))
    try:
        win = None
        doc.Activate()
        try:
            win = doc.ActiveWindow
        except:
            pass
        if win:
            win.Activate()
            table.Cell(row, col).Range.Text = text
    except Exception as e:
        raise Exception('{0}{1}'.format(prefix, e))

