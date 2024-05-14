from anvil import *
import anvil.server
import re


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def btnSapXep_click(self, **event_args):
    """This method is called when the button is clicked"""
    if(bool(re.fullmatch(r'\d+', self.txtNhapN.text))):
      if(self.rbSelectionSort.selected):
        self.txtKetQua.text = self.selection_sort(self.laySo(self.txtNhapN.text))
      elif(self.rbInsertionSort.selected):
        self.txtKetQua.text = self.insertion_Sort(self.laySo(self.txtNhapN.text))
      elif(self.rbBubbleSort.selected):
        self.txtKetQua.text = self.bubble_sort(self.laySo(self.txtNhapN.text))
      elif(self.rbMergeSort.selected):
        self.txtKetQua.text = self.merge_sort(self.laySo(self.txtNhapN.text))
    else:
      alert("Dữ liệu không hợp lệ")
    
  def insertion_Sort(self, arr):
    for i in range(1, len(arr)):
      key = arr[i]
      j = i - 1
      while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
      arr[j + 1] = key
    return arr

  def selection_sort(self, arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

  def bubble_sort(self, arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

  def merge_sort(self, arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        self.merge_sort(L)
        self.merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr
  
  def laySo(self, number):
      so = []
      for char in str(number):
        so.append(int(char))
      return so
