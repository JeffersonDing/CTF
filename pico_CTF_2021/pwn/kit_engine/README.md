# Kit Engine

This is a `V8` engine challenge and the key observation is the patch file that is used to compile the engine. Looking at the `patch` file in the source, we see a function called `AssembleEngine`. This is a function that we could call and looking at it, we see that it basically takes in an array of floating point numbers and runs it as a function.

```cpp
void Shell::AssembleEngine(const v8::FunctionCallbackInfo<v8::Value> &args)
{
   Isolate *isolate = args.GetIsolate();
   if (args.Length() != 1)
   {
      return;
   }

   double *func = (double *)mmap(NULL, 4096, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
   if (func == (double *)-1)
   {
      printf("Unable to allocate memory. Contact admin\n");
      return;
   }

   if (args[0]->IsArray())
   {
      Local<Array> arr = args[0].As<Array>();

      Local<Value> element;
      for (uint32_t i = 0; i < arr->Length(); i++)
      {
         if (arr->Get(isolate->GetCurrentContext(), i).ToLocal(&element) && element->IsNumber())
         {
            Local<Number> val = element.As<Number>();
            func[i] = val->Value();
         }
      }

      printf("Memory Dump. Watch your endianness!!:\n");
      for (uint32_t i = 0; i < arr->Length(); i++)
      {
         printf("%d: float %f hex %lx\n", i, func[i], doubleToUint64_t(func[i]));
      }

      printf("Starting your engine!!\n");
      void (*foo)() = (void (*)())func;
      foo();
   }
   printf("Done\n");
}
```

## Method

Now, we just need to inject some shellcode into it by converting into a floating point. `pwntools shellcraft` lets us do that very easily. After converting it into floats and doing some manipulation to get rid of edge cases, we just need to connect to the remote and let `pwntools` do the job.  
Finally, we will need an interactive shell, so by calling `bash 1>&0 2>&0` we get a shell. Technically, we could `cat flag.txt` but somehow it segfaults.
