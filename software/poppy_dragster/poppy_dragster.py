from poppy.creatures import AbstractPoppyCreature



class PoppyDragster(AbstractPoppyCreature):
    @classmethod
    def setup(cls, robot):
        def drive(speed):
            robot.l_wheel.moving_speed = speed
            robot.r_wheel.moving_speed = -speed

        def stop():
            drive(0)

        robot.drive = drive
        robot.stop = stop
