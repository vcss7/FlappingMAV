# FlappingMAV 
Optimizing the lift-to-drag ratio of flapping micro-air vehicles.

This repository aims to provide a guide to running an Unsteady Vortex Lattice
Method Simulation on the kinematics of flapping wings on a micro-air vehicle
The goal is to optimize the flapping motion to maximize the lift-to-drag ratio
by using the VTDIRECT95 optimization algorithm.

We will attempt to replicate the results found in the study conducted by Mehdi
Ghommem, Muhammad R. Hajj, Layne T. Watson, Dean T. Mook, Richard D. Snyder and
Philip S. Beran titled Deterministic Global Optimization of Flapping Wing
Motion for Micro Air Vehicles in 2010. DOI:
https://arc.aiaa.org/doi/10.2514/6.2010-9355

Unfortunately, the study does not have accompanying code and therefore other
software was found.

## Delta

How do we log into Delta?

How do we run a job on Delta?

## DIRECT Search Algorithm
A search algorithm that searches for coordinates (i.e. inputs) in a sample set
that generates the minumun value from a function that has little to no
randomness.

DIRECT is short for DIvide RECTangle and is named after the method of search that
it uses.

#### General Algorithm
1. Start with a sample search space.
1. Select one of the rectangles.
1. Divide into (3) rectangles.
1. Sample center of rectangles.
1. Repeat from step 2.

## VTDIRECT95

VTDIRECT95 is an algorithm that is based off of the DIRECT algorithm and adds
optimizations for faster and better performance. Both methods use a divide and
conquer approach and find a global maximum or minimum by dividing a search
space into rectangles and looking for the global maximum or minimum in those
sub regions.

There algorithms are numerical solutions and are used in places where
analytical solutions are difficult. In the case of finding the maximum
lift-to-drag ratio based off of non-geometrical parameters of a wing, a
numerical solution is needed because the complex aerodynamic equations make it
difficult to use analytical solutions.

Design parameters are the parameters to input values to that will generate the
search space for the VTDIRECT95 algorithm.

The design parameters for maximizing the lift-to-drag ratio of a flapping wing
that are considered are seven in total.
1. The amplitude in the x direction of the flapping motion
1. The amplitude in the y direction of the flapping motion
1. The amplitude of the rotation of the flapping motion
1. The phase angle in the x direction of the flapping motion
1. The phase angle in the y direction of the flapping motion
1. The phase angle of the rotation of the flapping motion
1. The change of inclination of the wing as the flapping motion switches
   direction (not entirely sure)

The amplitude can be defined as the difference between the maximum point and
the minimum point of the flapping motion.

The phase angle gives information about the timing and position of the flapping
motion of the wing relative to the initial time and position (I don't know how
to exactly define this)

The seventh parameter I'm still having trouble understanding and defining as
well.

Giving reasonable lower and upper bounds to the parameters aids in keeping a
reasonable search space. The paper provides the lower and upper bounds for the
parameters which will also be used here:

| Parameter | Lower | Upper |
|-----------|-------|-------|
| A_x       | 1     | 2     |
| A_y       | 0     | 1     |
| A_theta   | 20    | 70    |
| phi_x     | 0     | 360   |
| phi_y     | 0     | 360   |
| phi_theta | 0     | 360   |
| kappa     | 1     | 4     |


How are we linking the UVLM simulation (implemented in python) with the
VTDIRECT95 algorithm?

How does the professors code link the simulation with the VTDIRECT95 algorithm?

## Unsteady Vortex Lattice Method

The Unsteady Vortex Lattice Method (UVLM) is a Computational Fluids Dynamic
(CFD) simulation that models aerodynamic forces on an object, in this case, a
wing. It is suitable to use the Unsteady Vortex Lattice Method over the Steady
Vortex Lattice Method because the Unsteady Vortex Lattice Method accounts for
time variation or motion of the wings. In our application, this is important
because it allows for taking into account the flapping motion of our MAV.

The Unsteady term in the name of the method is referring to taking into account
flapping motion of the wing vs. not taking it into account (i.e. steady)

The Vortex term in the name of the method is referring to using vortices along
with the Biot-Savart Law to calculate forces on the object (wing).

The Lattice term in the name of the method is referring to the use of a lattice
pattern (i.e. panels) to divide the surface of the object (wing) and calculate
forces on the subdivisions. Each subdivision is represented by a thread that
runs along the surface and the "flow field" that these threads create is the
representation of the geometry and kinematics of the object.


What principles does it consider and use to run the simulation? What is the
Biot-Savart Law and why is it important in this context? Biot-Savart Law
relates the velocity of air at some point away from a vortex and the strength
of the vortex. In this context it is important because this kind of simulation
simulates vortices and the velocity of air around the wing affects the lift and
drag generated by the wings

What is the no-slip boundary condition and why is it important in this context?
No slip boundary condition is the assumption that the velocity of the air at
the surface of the wings is zero. This creates vortices because the air is
deflected off of the surface of the wing.

What kind of UVLM simulation was conducted in the paper? The kind of
simulations conducted in the paper are Unsteady Line Vortex Lattice Method
which represents the simulated vortices as lines perpendicular to the surface
of the wing. There are other UVLM simulations that represent the vortices as
rings or horseshoes. Those simulations are usually more computationally heavy
but are give more accurate results.

What geometry for the wing was used in the study? The geometry of the wing is
never specified

What kind of input does the simulation we are running take?

What kind of output does the simulation we are running give?
