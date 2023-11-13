!INCLUDE "mpif.h"     ! MPI library functions.
! This file (objfunc.f95) contains one objective function (CL) for pVTdirect.

! For all the objective functions:
! On input:
! c     - Point coordinates.
!
! On output:
! f     - Function value at 'c'.
! iflag - A flag that is used to indicate the status of the
!         function evaluation. It is 0 for normal status.
!
! Obj_CL:
! This function maximize the mean value of the lift coeffecient (mean(C_L))
! of a Flapping Micro Air Vehicle
! obj_CL = max(mean(C_L))
!


FUNCTION  Obj_CL(c, proc_id, iflag) RESULT(f)
USE REAL_PRECISION, ONLY : R8
IMPLICIT NONE

! Dummy variables.
REAL(KIND = R8), DIMENSION(:), INTENT(IN):: c
INTEGER, INTENT(OUT):: iflag
REAL(KIND = R8):: f

INTEGER, INTENT(IN):: proc_id
character (len=8) :: test_name
CHARACTER(len=30) :: filename
CHARACTER(len=60) :: fn1
CHARACTER(len=60) :: fn2
CHARACTER(len=60) :: fn3
CHARACTER(len=60) :: fn4
CHARACTER(len=60) :: fn5
! Local variables.
INTEGER:: i
INTEGER:: unt1
INTEGER:: iostat
LOGICAL:: opened

! Abhishek: Update PAR(n) n=dimension
REAL*8::PAR(5)
     write (test_name, '( "test_", I3.3)' ) proc_id
     call system ( "mkdir " //test_name)
! Abhishek: Change DO i=2,N when using N parameter optimization
! c(1) is the water radius and c(i=2,6) are the sum of water radius and the
! atomic radius, therefore one must pass the difference in the input parameters
! c(7) is tau parameter in CHAGB

! PAR(1)=c(1)             ! water radius
! DO i=2,5
! PAR(i) = c(i) -c(1)     ! atomic radii
! ENDDO 

!filename = ''//test_name//"/param.txt"
     write (filename, '( "test_",I3.3,"/param.txt")' ) proc_id
     write (fn1, '( "cp RunUVLM.sh ./test_",I3.3,"/.")' ) proc_id
     write (fn2, '( "cd test_",I3.3," ; ./RunUVLM.sh ; cd ..")' ) proc_id
     write (fn3, '( "cat test_",I3.3,"/CL.dat >> CL.dat")' ) proc_id
     write (fn4, '( "rm -rf test_",I3.3)' ) proc_id
     write (fn5, '( "test_",I3.3,"/CL.dat")' ) proc_id
! Check if unit is open
      do unt1 = 17,1,-1
         inquire (unit=unt1, opened=opened, iostat=iostat)
         if (iostat.ne.0) cycle
         if (.not.opened) exit
      end do

OPEN (UNIT=unt1,FILE=filename,ACTION="write",STATUS="replace")
! Abhishek: Change DO i=1,N when using N parameter optimization
DO i=1,5
  WRITE(unt1,*) PAR(i)
!  WRITE(*,*) PAR(i)
ENDDO
CLOSE (unt1)
call system (""//fn1)
call system (""//fn2)
! Check if UNIT is open      
do unt1 = 17,1,-1
    inquire (unit=unt1, opened=opened, iostat=iostat)
    if (iostat.ne.0) cycle
    if (.not.opened) exit
end do
OPEN(UNIT=unt1,FILE=fn5)
  READ(unt1,*) f
iflag = 0
CLOSE (unt1)
call system (""//fn3)
call system (""//fn4)
call system (""//fn4)

RETURN
END FUNCTION Obj_CL
