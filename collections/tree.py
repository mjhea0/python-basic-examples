#coding:utf-8

class Treenode:
   def __init__( self, data ):
      self._left = None
      self._data = data
      self._right = None

   def __str__( self ):
      return str( self._data )      

class Tree:
   def __init__( self ):
      self._rootNode = None
        
   def insertNode( self, value ):
      if self._rootNode is None:  
         self._rootNode = Treenode( value )
      else: 
         self.insertNodeHelper( self._rootNode, value )

   def insertNodeHelper( self, node, value ):
      if value < node._data: 
         if node._left is None:
            node._left = Treenode( value )
         else:
            self.insertNodeHelper ( node._left, value )
      elif value > node._data:
         if node._right is None: 
            node._right = Treenode( value )
         else:
            self.insertNodeHelper( node._right, value )
      else: 
         print value, "duplicate"

   def preOrderTraversal( self ):
      self.preOrderHelper( self._rootNode )

   def preOrderHelper( self, node ):
      if node is not None:
         print node,
         self.preOrderHelper( node._left )
         self.preOrderHelper( node._right )

   def inOrderTraversal( self ):
      self.inOrderHelper( self._rootNode )

   def inOrderHelper( self, node ):
      if node is not None:
         self.inOrderHelper( node._left )
         print node,
         self.inOrderHelper( node._right )

   def postOrderTraversal( self ):
      self.postOrderHelper( self._rootNode )

   def postOrderHelper( self, node ):
      if node is not None:
         self.postOrderHelper( node._left )
         self.postOrderHelper( node._right )
         print node,
         
tree = Tree()
values = "1 2 3 4 5 6 7 8 9 0 10"

for i in values.split():
   tree.insertNode( int( i ) )

tree.preOrderTraversal()
print

tree.inOrderTraversal()
print

tree.postOrderTraversal()
print
