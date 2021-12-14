program solout
!=========================================================================================
! Simple solitaire output generator. 
!
! From the command line, this program takes 55 arguments, all integers.
! The first number is the number of outputs requested. The next 54 are
! the card values in the deck order. 
!
! Daniel A. Brue, October 2013
! dabrue@us.ibm.com
!=========================================================================================
implicit none

integer, parameter :: i1_kind = selected_int_kind(2)
integer(kind=i1_kind), parameter :: jA = 53
integer(kind=i1_kind), parameter :: jB = 54
integer(kind=i1_kind) :: i, j, k, l, m, n
integer(kind=i1_kind) :: jA_index, jB_index
integer(kind=i1_kind) :: Deck0(54), Deck1(54)
integer :: nargs
integer :: noutput, nout
character(len=32) :: arg

nargs = iargc()

if (nargs < 55) then
    print*, "Insufficient arguments"
    print*, nargs
    call exit(1)
endif

! Get the first number in the list, the number of requested outputs
call getarg(1,arg)
read(arg,"(I32)") noutput

! Get the other 54 arguments which are the cards in initial deck order
do i=1,54
    j=i+1
    call getarg(j,arg)
    read(arg,"(I32)") Deck0(i)
enddo

nout = 0

do while(nout < noutput)
    ! Move jokers
    do j=1,54
        if (Deck0(j) == 53) then
            jA_index = j
            exit
        endif
    enddo
    if (jA_index == 54) then
        Deck1(1)=Deck0(1)
        Deck1(2)=jA
        Deck1(3:54) = Deck0(2:53)
        Deck0=Deck1
    else
        l = Deck0(jA_index+1)
        Deck0(jA_index+1) = Deck0(jA_index)
        Deck0(jA_index) = l
    endif 
    do j=1,54
        if (Deck0(j) == 54) then
            jB_index = j
            exit
        endif
    enddo
    if (jB_index == 54) then
        Deck1(1:2) = Deck0(1:2)
        Deck1(3) = 54
        Deck1(4:54) = Deck0(3:53)
        Deck0=Deck1
    else if (jB_index==53) then
        Deck1(1) = Deck0(1)
        Deck1(2) = 54
        Deck1(3:53) = Deck0(2:52)
        Deck1(54) = Deck0(54)
        Deck0=Deck1
    else
        k=Deck0(jB_index+1)
        l=Deck0(jB_index+2)
        Deck0(jB_index+2) = jB
        Deck0(jB_index+1) = l
        Deck0(jB_index) = k
    endif

    ! now triple cut
    do j=1,54
        if (Deck0(j) == 53) then
            jA_index = j
        else if (Deck0(j) == 54) then
            jB_index = j
        endif
    enddo
    k = min(jA_index,jB_index)
    l = max(jA_index,jB_index)
    m = l-k+1
    n = 54-l
    Deck1(1:n)=Deck0(l+1:54)
    Deck1(n+1:n+m) = Deck0(k:l)
    Deck1(n+m+1:54) = Deck0(1:k-1)
    Deck0=Deck1

    ! now count cut
    k = Deck0(54)
    if (k == 54) k = 53
    l=53-k
    Deck1(1:l) = Deck0(k+1:53)
    Deck1(l+1:53) = Deck0(1:k)
    Deck1(54) = Deck0(54)
    Deck0=Deck1

    ! Get output
    k = Deck0(1)
    if (k == 54) k = 53
    k = k + 1
    m = Deck0(k)
    if (m == 53 .or. m == 54) then
        cycle
    else
        nout = nout + 1
        print*, m
    endif
enddo

end program

