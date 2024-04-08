# reto5

there's two folders , one called unique_module where the shape_package just have the shape module and all the classes needed are imported in form the shape module


The other folder called individual_modules has a package "children_of_shape" where is found shape, rectangle and triangle modules , triangle and rectangle have relative imports of shape and main has absolute imports either from triangle and rectangle

maybe it doesn't matter to you but took me long time realised that I needed to have relative imports in rectangle and triangle for the code to work
