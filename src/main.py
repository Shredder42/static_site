from textnode import TextNode
from textnode import TextType
from htmlnode import LeafNode
            

def main():
    new_node = TextNode('Ghost is my dog', TextType.ITALIC, 'http://www.mlb.com')
    print(repr(new_node))


if __name__ == '__main__':
    main()
