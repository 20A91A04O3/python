{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPyctpvXzr54Zp3OODcwDzo"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "no8hJXXa3ay1",
        "outputId": "0f4bb2c4-fe80-4272-9de8-d2848fbec99a"
      },
      "source": [
        "def fun(n):\n",
        "  if n<=0:\n",
        "    print(n,end=\" \")\n",
        "    return\n",
        "  fun(n-1)\n",
        "  fun(n-2)\n",
        "  print(n,end=\" \")\n",
        "fun(5)"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0 -1 1 0 2 0 -1 1 3 0 -1 1 0 2 4 0 -1 1 0 2 0 -1 1 3 5 "
          ]
        }
      ]
    }
  ]
}