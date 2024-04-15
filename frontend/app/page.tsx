"use client"
import UploadForm from "@/components/UploadForm";
import ArleyPeter from "@/components/ArleyPeter";
import ViLy from "@/components/ViLy";
import { Progress } from "@/components/ui/progress"


import { useState, useEffect } from "react"

export default function Home() {

  const [buttonClicked, setButtonClicked] = useState(false);

  const handleButtonClick = () => {
    setButtonClicked(true);
    console.log('Button clicked in UploadForm!');
  };

  const [progressValue, setProgressValue] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      if (progressValue < 100) {
        setProgressValue(prevValue => prevValue + 1);
      } else {
        clearInterval(interval);
      }
    }, 50);

    return () => {
      clearInterval(interval);
    };
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1 className="text-4xl font-bold">HemoCountAI</h1>
      {buttonClicked ? <Progress value={progressValue} /> : <UploadForm onButtonClick={handleButtonClick} />}
      <p className="font-light">By <ViLy/> and <ArleyPeter/>.</p>
    </main>
  );
}
