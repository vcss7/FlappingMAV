"""
This script runs an unsteady ring vortex lattice method solver on a custom
ornithopter with static geometry.
"""

import pterasoftware as ps

# The geometry coordinates are defined as such: If you were riding in the
# airplane, the positive x direction would point behind you, the positive y
# direction would point out of your right wing, and the positive z direction
# would point upwards, out of your chair. These directions form a right-handed
# coordinate system.

# Settings that were changed from the default values are commented with
# "FlappingMAV setting".

# NOT possible to set phase angles of flapping motion

# Simulation settings
TIME_STEP = 0.02

# Wing geometry settings
CHORD_LENGTH = 1.0
NUM_CHORDWISE_PANELS = 16
NUM_SPANWISE_PANELS = 16

# Define the flapping motions of the wing.
# amplitudes of flapping motion
AMP_X = 1.0
AMP_Y = 0.0
AMP_ROT = 40.0

# phase of flapping motion
PHI_X = 0.0
PHI_Y = 0.0
PHI_ROT = 3.14159/2

# frequencies of flapping motion
FREQ_X = 1.0
FREQ_ROT = 1.0

# Create an airplane object.
ornithopter = ps.geometry.Airplane(
    name="Hummingbird",

    # Define the location of the airplane's center of gravity relative to the
    # global coordinate system fixed front left corner of the first airplane's
    # first wing's root wing cross section.
    x_ref=0.0,
    y_ref=0.0,
    z_ref=0.0,

    # Define the reference area, span, and chord of this airplane. These values
    # default to None, which will cause them to be calculated from the wing
    # geometry.
    # Note that the reference area used in this program is the wetted area of
    # the wing's mean-camberline surface.
    s_ref=None,
    b_ref=None,
    c_ref=None,

    # List the wings that comprise this airplane. Each wing is its own object.
    wings=[
        # Create a new wing object.
        ps.geometry.Wing(
            # Give the wing a name, this defaults to "Untitled Wing".
            name="Main Wing",
            # Define the location of the leading edge of the wing relative to
            # the global coordinate system fixed front left corner of the first
            # airplane's first wing's root wing cross section. These values all
            # default to 0.0 meters.
            x_le=0.0,
            y_le=0.0,
            z_le=0.0,

            # Declare that this wing is symmetric.
            symmetric=True,

            # Define the number of chordwise panels on the wing, and the
            # spacing between them.
            num_chordwise_panels=NUM_CHORDWISE_PANELS,    # FlappingMAV setting
            chordwise_spacing="uniform",

            # List the wing cross sections that comprise this wing. Each wing
            # must have at least two wing cross sections.
            wing_cross_sections=[
                # Create a new wing cross section object.
                ps.geometry.WingCrossSection(
                    # Define the location of the leading edge of the wing cross
                    # section relative to the wing's leading edge.
                    x_le=0.0,
                    y_le=0.0,
                    z_le=0.0,

                    # Define the twist of the wing cross section in degrees.
                    # This is equivalent to incidence angle of cross section.
                    # The twist is about the leading edge.
                    # Positive twist corresponds to positive rotation about the
                    # y axis, as defined by the right-hand rule.
                    twist=0.0,     # FlappingMAV setting

                    # Define the type of control surface. The options are
                    # "symmetric" and "asymmetric". This is only applicable if
                    # your wing is also symmetric.
                    control_surface_type="symmetric",

                    # Define the control surface hinge point. This is expressed
                    # as a fraction of the chord length, back from the leading
                    # edge. The default value is 0.75.
                    control_surface_hinge_point=0.75,

                    # Define the deflection of the control surface in degrees.
                    control_surface_deflection=0.0,

                    # Define the number of spanwise panels on the wing cross
                    # section, and the spacing between them.
                    num_spanwise_panels=NUM_SPANWISE_PANELS,
                    spanwise_spacing="uniform",

                    # Set the chord of this cross section to be 1.00 meters.
                    chord=CHORD_LENGTH,     # FlappingMAV setting

                    # Every wing cross section has an airfoil object.
                    airfoil=ps.geometry.Airfoil(
                        # Give the airfoil a name.
                        # This name should correspond to a name in the airfoil
                        # directory or a NACA four series airfoil.
                        name="ag03",

                        # Define a custom airfoil. Leave as None to use an
                        # airfoil from the airfoil directory.
                        coordinates=None,

                        # This is the variable that determines whether you
                        # would like to repanel the airfoil coordinates.
                        repanel=True,

                        # This is number of points to use if repaneling the
                        # airfoil. It is ignored if the repanel is False.
                        n_points_per_side=400,
                    ),
                ),
                # Define the next wing cross section.
                ps.geometry.WingCrossSection(
                    x_le=0.75,
                    y_le=6.0,
                    z_le=1.0,
                    chord=CHORD_LENGTH,     # FlappingMAV setting
                    twist=0.0,    # FlappingMAV setting
                    # Give this wing cross section an airfoil.
                    airfoil=ps.geometry.Airfoil(
                        name="ag03",
                    ),
                ),
            ],
        ),
    ],
)

# Define the main wing's root wing cross section's movement.
# Cross sections can move in three ways: sweeping, pitching, and heaving.
# Sweeping is defined as the relative rotation of this wing cross section's
#   leading edge to its preceding wing cross section's leading edge about the
#   airplane's body x axis.
# Pitching is defined as the relative rotation of this wing cross section's
#   leading edge to the preceding wing cross section's leading edge about the
#   body y axis.
# Heaving is defined as the relative rotation of this wing cross section's
#   leading edge to the preceding wing cross section's leading edge about the
#   body z axis.
# The sign of all rotations is determined via the right-hand-rule.
main_wing_root_wing_cross_section_movement = ps.movement.WingCrossSectionMovement(
    # Provide the base cross section.
    base_wing_cross_section=ornithopter.wings[0].wing_cross_sections[0],

    # Define the sweeping amplitude. This value is in degrees. As this is the
    # first wing cross section, this must be 0.0 degrees.
    sweeping_amplitude=0.0,

    # Define the sweeping period. This value is in seconds. As this is the 
    # first wing cross section, this must be 0.0 seconds.
    sweeping_period=0.0,

    # Define the time step spacing of the sweeping.
    # The options are "sine" and "uniform".
    sweeping_spacing="sine",

    # Define the pitching amplitude. This value is in degrees. As this is the
    # first wing cross section, this must be 0.0 degrees.
    pitching_amplitude=0.0,

    # Define the pitching period. This value is in seconds. As this is the
    # first wing cross section, this must be 0.0 seconds.
    pitching_period=0.0,

    # Define the time step spacing of the pitching.
    # The options are "sine" and "uniform".
    pitching_spacing="sine",

    # Define the heaving amplitude. This value is in degrees. As this is the
    # first wing cross section, this must be 0.0 degrees.
    heaving_amplitude=0.0,

    # Define the heaving period. This value is in seconds. As this is the
    # first wing cross section, this must be 0.0 seconds.
    heaving_period=0.0,

    # Define the time step spacing of the heaving.
    # The options are "sine" and "uniform".
    heaving_spacing="sine",
)

# Define the main wing's tip wing cross section's movement.
main_wing_tip_wing_cross_section_movement = ps.movement.WingCrossSectionMovement(
    base_wing_cross_section=ornithopter.wings[0].wing_cross_sections[1],
    sweeping_amplitude=0.0,
    sweeping_period=0,
    sweeping_spacing="sine",
    pitching_amplitude=AMP_ROT,
    pitching_period=FREQ_ROT,
    pitching_spacing="sine",
    heaving_amplitude=0.0,
    heaving_period=0.0,
    heaving_spacing="sine",
)

# Define the main wing's movement. In addition to their wing cross sections'
# relative movements, wings' leading edge positions can move as well.
main_wing_movement = ps.movement.WingMovement(
    # Define the base wing object.
    base_wing=ornithopter.wings[0],

    # Add the list of wing cross section movement objects.
    wing_cross_sections_movements=[
        main_wing_root_wing_cross_section_movement,
        main_wing_tip_wing_cross_section_movement,
    ],

    # Define the amplitude of the leading edge's change in x position (meters).
    x_le_amplitude=AMP_X,

    # Define the period of the leading edge's change in x position (seconds)
    x_le_period=FREQ_X,

    # Define the time step spacing of the leading edge's change in x position.
    # The options are "sine" and "uniform".
    x_le_spacing="sine",

    # Define the amplitude of the leading edge's change in y position (meters).
    y_le_amplitude=AMP_Y,

    # Define the period of the leading edge's change in y position (seconds)
    y_le_period=0.0,

    # Define the time step spacing of the leading edge's change in y position.
    # The options are "sine" and "uniform".
    y_le_spacing="sine",

    # Define the amplitude of the leading edge's change in z position (meters).
    z_le_amplitude=0.0,

    # Define the period of the leading edge's change in z position (seconds)
    z_le_period=0.0,

    # Define the time step spacing of the leading edge's change in z position.
    # The options are "sine" and "uniform".
    z_le_spacing="sine",
)

# Delete the extraneous wing cross section movement objects, as these are now
# contained within the wing movement object.
del main_wing_root_wing_cross_section_movement
del main_wing_tip_wing_cross_section_movement

# Define the airplane's movement object.
airplane_movement = ps.movement.AirplaneMovement(
    # Define the base airplane object.
    base_airplane=ornithopter,

    # Add the list of wing movement objects.
    wing_movements=[main_wing_movement],

    # Define the amplitude of the reference position's change in x position
    # (meters).
    x_ref_amplitude=0.0,

    # Define the period of the reference position's change in x position
    # (seconds).
    x_ref_period=0.0,

    # Define the time step spacing of the reference position's change in x
    # position.
    # The options are "sine" and "uniform".
    x_ref_spacing="sine",

    # Define the amplitude of the reference position's change in y position
    # (meters).
    y_ref_amplitude=0.0,

    # Define the period of the reference position's change in y position
    # (seconds).
    y_ref_period=0.0,

    # Define the time step spacing of the reference position's change in y
    # position.
    # The options are "sine" and "uniform".
    y_ref_spacing="sine",

    # Define the amplitude of the reference position's change in z position
    # (meters).
    z_ref_amplitude=0.0,

    # Define the period of the reference position's change in z position
    # (seconds).
    z_ref_period=0.0,

    # Define the time step spacing of the reference position's change in z
    # position.
    # The options are "sine" and "uniform".
    z_ref_spacing="sine",
)

# Delete the extraneous wing movement objects, as these are now contained
# within the airplane movement object.
del main_wing_movement

# Define a new operating point object. This defines the state at which the airplane
# object is operating.
example_operating_point = ps.operating_point.OperatingPoint(
    # Define the density of the fluid the airplane is flying in.
    # This defaults to 1.225 kilograms per meters cubed.
    density=1.225,

    # Define the angle of sideslip the airplane is experiencing.
    beta=0.0,

    # Define the freestream velocity at which the airplane is flying.
    velocity=10.0,

    # Define the angle of attack the airplane is experiencing.
    alpha=1.0,

    # Define the kinematic viscosity of the air in meters squared per second.
    # This defaults to 15.06e-6 meters squared per second, which corresponds to
    # an air temperature of 20 degrees Celsius.
    nu=15.06e-6,
)

# Define the operating point's movement. The operating point's velocity can
# change with respect to time.
operating_point_movement = ps.movement.OperatingPointMovement(
    # Define the base operating point object.
    base_operating_point=example_operating_point,

    # Define the amplitude of the velocity's change in time.
    velocity_amplitude=0.0,

    # Define the period of the velocity's change in time.
    velocity_period=0.0,

    # Define the time step spacing of the velocity's change in time.
    # The options are "sine" and "uniform".
    velocity_spacing="sine",
)

# Define the movement object. Contains the airplane movement and the operating
# point movement.
movement = ps.movement.Movement(
    # Add the airplane movement.
    airplane_movements=[airplane_movement],

    # Add the operating point movement.
    operating_point_movement=operating_point_movement,

    # Leave the number of time steps and the length of each time step as None.
    # The solver will automatically set the length of the time steps so that
    # the wake ring vortices and the bound ring vortices have approximately the
    # same area. The solver will also determine if the geometry is static or
    # not. If it is static, the number of steps will be set such that the wake
    # extends ten chord lengths back from the main wing. If the geometry isn't
    # static, the number of steps will be set such that three periods of the
    # slowest movement oscillation complete.
    num_steps=None,
    delta_time=TIME_STEP,
)

# Delete the extraneous airplane and operating point movement objects, as these
# are now contained within the movement object.
del airplane_movement
del operating_point_movement

# Define the unsteady hummingbird problem.
unsteady_hummingbird_problem = ps.problems.UnsteadyProblem(
    movement=movement,
)

# Define a new solver.
uvlm_solver = ps.unsteady_ring_vortex_lattice_method.UnsteadyRingVortexLatticeMethodSolver(
    # Solvers just take in one attribute: the problem they are going to solve.
    unsteady_problem=unsteady_hummingbird_problem,
)

# Delete the extraneous pointer to the problem as it is now contained within
# the solver.
del unsteady_hummingbird_problem

# Run the example solver.
uvlm_solver.run(
    # This parameter determines the detail of information that the solver's
    # logger will output while running. The options are, in order of detail and
    # severity, "Debug", "Info", "Warning", "Error", "Critical".
    # The default value is "Warning".
    logging_level="Warning",

    # Use a prescribed wake model. This is faster, but may be less accurate.
    prescribed_wake=True,
)

#"""
# Call the software's draw function on the solver.
# Press "q" to close the plotter after it draws the output.
ps.output.draw(
    # Set the solver to the one we just ran.
    solver=uvlm_solver,

    # Tell the draw function to color the aircraft's wing panels with the local
    # lift coefficient. The valid arguments for this parameter are None,
    # "induced drag", "side force", or "lift".
    scalar_type="lift",

    # Tell the draw function to show the calculated streamlines.
    show_streamlines=True,

    # Tell the draw function to not show the wake vortices.
    show_wake_vortices=False,

    # Tell the draw function to not save the drawing as an image file. The
    # drawing will still be displayed but not saved.
    save=False,
)

# Call the software's animate function on the solver. This produces a GIF of
# the wake being shed.
# Press "q", after orienting the view, to begin the animation.
ps.output.animate(
    # Set the unsteady solver to the one we just ran.
    unsteady_solver=uvlm_solver,

    # Tell the animate function to color the aircraft's wing panels with the
    # local lift coefficient. The valid arguments for this parameter are None,
    # "induced drag", "side force", or "lift".
    scalar_type="lift",

    # Tell the animate function to show the wake vortices.
    show_wake_vortices=True,

    # Tell the animate function to not save the animation as file. The
    # animation will still be displayed but not saved.
    save=True,
)

# Call the software's plotting function on the solver. This produces graphs of
# the output forces and moments with respect to time.
ps.output.plot_results_versus_time(
    # Set the unsteady solver to the one we just ran.
    unsteady_solver=uvlm_solver,

    # Set the show attribute to True.
    show=True,
    save=False,
)
#"""

ps.output.print_unsteady_results(
    # Set the unsteady solver to the one we just ran.
    unsteady_solver=uvlm_solver,
)
