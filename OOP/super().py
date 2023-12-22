this method works as a proxy to be able to access the parent/self class,  e.g
special


cls like self but cls is a keyword that's used to access a class method, which is a code template for creating objects. self is a keyword that's used to access an instance method
cls is generally used in the __new__ special staticmethod, or in classmethods, which you make similarly to staticmethods. These are methods that only need access to the class, but not to things specific to each instance of the class.
