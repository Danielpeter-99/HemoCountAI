'use client'
import * as React from "react"

import {
  InputOTP,
  InputOTPGroup,
  InputOTPSlot,
} from "@/components/ui/input-otp"

export default function Home() {
  const [value, setValue] = React.useState("")

  React.useEffect(() => {
    if (value.length === 6 && value === "123456") {
      window.location.href = "/dashboard"
    }
  }, [value])

  return (
    <main className="flex flex-col items-center justify-between p-24">
      <InputOTP
        maxLength={6}
        value={value}
        onChange={(value: any) => setValue(value)}
      >
        <InputOTPGroup>
          <InputOTPSlot index={0} />
          <InputOTPSlot index={1} />
          <InputOTPSlot index={2} />
          <InputOTPSlot index={3} />
          <InputOTPSlot index={4} />
          <InputOTPSlot index={5} />
        </InputOTPGroup>
      </InputOTP>
      <div className="mt-5">Enter your one-time password.</div>
    </main>
  )
}
