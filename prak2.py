{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "65178885-32cc-47f4-b3b1-9181ba0a7525",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Plain Text is : HELLO EVERYONE\n",
      "Shift pattern is : 1\n",
      "Cipher Text is : IFMMP FWFSZPOF\n"
     ]
    }
   ],
   "source": [
    "def encrypt_text(plaintext, n):\n",
    "    ans = \"\"\n",
    "    for i in range(len(plaintext)):\n",
    "        ch = plaintext[i]\n",
    "        if ch == \" \":\n",
    "            ans += \" \"\n",
    "        elif ch.isupper():\n",
    "            ans += chr((ord(ch) + n - 65) % 26 + 65)\n",
    "        else:\n",
    "            ans += chr((ord(ch) + n - 97) % 26 + 97)\n",
    "    return ans\n",
    "\n",
    "plaintext = \"HELLO EVERYONE\"\n",
    "n = 1\n",
    "print(\"Plain Text is : \" + plaintext)\n",
    "print(\"Shift pattern is : \" + str(n))\n",
    "print(\"Cipher Text is : \" + encrypt_text(plaintext, n))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa878302-5589-4336-adfe-76236f876599",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}