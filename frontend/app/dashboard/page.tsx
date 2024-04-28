"use client"
import { useState, useEffect } from "react";
import Image from "next/image";

import UploadForm from "@/components/UploadForm";
import ArleyPeter from "@/components/ArleyPeter";
import BloodChart from "@/components/BloodChart";
import ViLy from "@/components/ViLy";
import { Progress } from "@/components/ui/progress";

import hemocount_logo from "@/public/hemocount-logo.png";

export default function Home() {
  const [buttonClicked, setButtonClicked] = useState(false);
  const [progressValue, setProgressValue] = useState(0);
  const [uploadComplete, setUploadComplete] = useState(false);
  const [bloodData, setBloodData] = useState<any>(null);

  const handleButtonClick = () => {
    setButtonClicked(true);
    console.log('Button clicked in UploadForm!');
  };

  const handleUploadComplete = (data: any) => {
    console.log('Upload complete:', data);
    setUploadComplete(true);
    setBloodData(data);
  };

  useEffect(() => {
    let interval: NodeJS.Timeout;

    const uploadProgress = () => {
      if (!uploadComplete && progressValue < 95) {
        setProgressValue(prevValue => prevValue + 1);
      } else if (uploadComplete && progressValue < 100) {
        setProgressValue(prevValue => prevValue + 5);
      } else {
        clearInterval(interval);
      }
    };

    interval = setInterval(uploadProgress, 100);

    return () => {
      clearInterval(interval);
    };
  }, [uploadComplete, progressValue]);

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <Image className="mb-5" src={hemocount_logo} alt="HemoCountAI Logo" />
      {buttonClicked ? (
        uploadComplete ? (
          <div>
          <BloodChart bloodData={bloodData} />
          </div>
        ) : (
          <Progress className="h-2 w-1/2" value={progressValue} />
        )
      ) : (
        <UploadForm onButtonClick={handleButtonClick} onUploadComplete={handleUploadComplete} />
      )}
      <p className="font-light">By <ViLy/> and <ArleyPeter/>.</p>
    </main>
  );
}
