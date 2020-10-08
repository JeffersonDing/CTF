int main(void)

{
  uint32_t i;
  int unused;
  _Bool pass;
  
  setbuf(stdout,(char *)0x0);
  setbuf(stdin,(char *)0x0);
  setbuf(stderr,(char *)0x0);
  puts("I hate my data structures class! Why can\'t I just sort by hand?");
  pass = false;
  while( true ) {
    scanf(nums);
    if (8 < i) break;
    nums[i] = nums[i] ^ nums[i + 1];
    nums[i + 1] = nums[i + 1] ^ nums[i];
    nums[i] = nums[i] ^ nums[i + 1];
    pass = check();
  }
  if (pass == false) {
    puts("Try again!");
  }
  else {
    puts("Well done!");
    print_flag();
  }
  return 0;
}
