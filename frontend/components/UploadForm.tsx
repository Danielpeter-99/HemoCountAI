import React, { useState } from 'react';
import { Upload } from 'lucide-react';

import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';

interface UploadFormProps {
    onButtonClick: () => void;
    onUploadComplete: (data: any) => void;
  }

function UploadForm({ onButtonClick, onUploadComplete }: UploadFormProps) {
    const [selectedFile, setSelectedFile] = useState<File | null>(null);
    const [buttonClicked, setButtonClicked] = useState(false);

const handleButtonClick = () => {
setButtonClicked(true);
onButtonClick();
};

const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
  const file = event.target.files?.[0] || null;
  
  if (file && !file.type.startsWith('image/')) {
    window.alert('File must be an image.');
    event.target.value = '';
    setSelectedFile(null);
  } else {
    setSelectedFile(file);
  }
};

  const handleSubmit = async () => {
    if (selectedFile) {
      try {
        handleButtonClick();
        const formData = new FormData();
        formData.append('file', selectedFile);

        const response = await fetch('http://localhost:5000/get_blood_cells', {
          method: 'POST',
          body: formData,
        });

        if (response.ok) {
          const responseData = await response.json();
          console.log('File uploaded successfully!');
          console.log(responseData);
          onUploadComplete(responseData); // Add this line
        } else {
          console.error('Error uploading file:', response.statusText);
        }
      } catch (error) {
        console.error('An error occurred:', error);
        window.alert('An error occurred: ' + (error as Error).message);
        window.location.reload();
      }
    } else {
      console.warn('No file selected.');
    }
  };

  return (
    <div className='flex flex-row'>
      <Input className='mr-3' type="file" accept="image/*" onChange={handleFileChange} />
      <Button variant={"outline"} onClick={handleSubmit}><Upload className='mr-2 h-4 w-4'/>Upload</Button>
    </div>
  );
}

export default UploadForm;
