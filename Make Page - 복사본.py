{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 코딩 도장 게시판 페이징 문제"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## A씨는 게시판 프로그램을 작성하고 있다.  \n",
    "## A씨는 게시물의 총 건수와 한 페이지에 보여줄 게시물수를 입력으로 주었을 때 총 페이지수를 리턴하는 프로그램이 필요하다고 한다.\n",
    "\n",
    "## __입력 : 총건수(m), 한페이지에 보여줄 게시물수(n) (단 n은 1보다 크거나 같다. n >= 1)__\n",
    "## __출력 : 총페이지수__\n",
    "\n",
    "## A씨가 필요한 프로그램을 작성하시오."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "> 총 건수를 입력하시오: 11\n",
      ">한 페이지에 보여줄 게시물 수를 입력하시오: 10\n",
      "11 10 2\n"
     ]
    }
   ],
   "source": [
    "m = int(input(\"> 총 건수를 입력하시오: \"))\n",
    "n = int(input(\">한 페이지에 보여줄 게시물 수를 입력하시오: \"))\n",
    "\n",
    "if n <= 0:\n",
    "    print((\"1이상의 수를 입력하시오.\"))\n",
    "    n = int(input(\">한 페이지에 보여줄 게시물 수를 입력하시오: \"))\n",
    "                            \n",
    "if m > n:\n",
    "    output = (m//n) + 1\n",
    "              \n",
    "elif m == n:\n",
    "    output = (m//n)\n",
    "              \n",
    "else:\n",
    "    ouput = (m//n) +1\n",
    "     \n",
    "print(m,n,output)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
