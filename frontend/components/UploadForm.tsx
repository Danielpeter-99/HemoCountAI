"use client"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { zodResolver } from "@hookform/resolvers/zod"

import { z } from "zod"
import { useForm } from "react-hook-form"
import { useState } from "react"

import { ImageUp  } from "lucide-react"


interface UploadFormProps {
  onButtonClick: () => void;
}

function UploadForm({ onButtonClick }: UploadFormProps) {

  const [buttonClicked, setButtonClicked] = useState(false);

    const formSchema = z.object({
        file: z.custom<File>(),
      })

    const form = useForm<z.infer<typeof formSchema>>({
        resolver: zodResolver(formSchema)})
      
    function onSubmit(values: z.infer<typeof formSchema>) {
        formSchema.parse(values)
        console.log(values)
      }

    const handleButtonClick = () => {
      setButtonClicked(true);
      onButtonClick();
    };
    

  return (
    <div className="flex flex-col items-center justify-center p-24">
    <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
      <div className="flex flex-col justify-center">
        <label htmlFor="file" className="block font-medium text-gray-700">
          Upload a File
        </label>
        <Input type="file" id="file" {...form.register("file")} />
        {form.formState.errors.file && (
          <p className="text-red-500">{form.formState.errors.file.message}</p>
        )}
    <Button className="mt-6" type="submit" onClick={handleButtonClick}>
      <ImageUp className="mr-2 h-4 w-4" /> Upload Image
    </Button>
      </div>
    </form>
    </div>
    )
}

export default UploadForm