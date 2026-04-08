from textnode import TextType 
from textnode import TextNode 

def main():
	textNode = TextNode("Boot Dev Link", TextType.LINK, "https://www.boot.dev")
	print(textNode)

main()
