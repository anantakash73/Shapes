
Repository contains implementations of a Shapes class according to [spec](https://docs.google.com/document/d/1ttefuYA_2XoUC3qQyFoMSQZI6bBBvs8LzY1Fem5G58k/edit) provided by Newfront Insurance

# Coordinate Space
Only one coordinate space can be created which is enforced by the use of a Singleton class

Once set, the coordinate space cannot be modified and neither can a new one be created

# Shapes

Three subclasses were created, namely Square, Triangle and Circle, derived from a Shapes class

When they are created, the bounds are checked to see if they can exist within the coordinate space
Tests for the same exist

Functionality being worked on was checking for collisons upon moving. The approach being taken was to compare the object being moved to every other existing Shape and check if there is a collison. 

