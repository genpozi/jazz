import React, { useState, useEffect } from 'react'
import { Button } from '../ui/button'
import { Input } from '../ui/input'
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription } from '../ui/dialog'

interface ChallengeDialogProps {
  onAuthenticated: () => void
}

export function ChallengeDialog({ onAuthenticated }: ChallengeDialogProps) {
  const [open, setOpen] = useState(false)
  const [answer, setAnswer] = useState('')
  const [error, setError] = useState('')
  const [attempts, setAttempts] = useState(0)

  useEffect(() => {
    // Check if user is already authenticated
    const isAuthenticated = sessionStorage.getItem('jaaz_challenge_authenticated')
    if (!isAuthenticated) {
      setOpen(true)
    } else {
      onAuthenticated()
    }
  }, [onAuthenticated])

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    
    // Check if answer is "jasper" (case-insensitive)
    if (answer.toLowerCase().trim() === 'jasper') {
      // Store authentication in sessionStorage (cleared when browser closes)
      sessionStorage.setItem('jaaz_challenge_authenticated', 'true')
      setOpen(false)
      setError('')
      onAuthenticated()
    } else {
      setAttempts(prev => prev + 1)
      setError(`Incorrect answer. Please try again. (Attempt ${attempts + 1})`)
      setAnswer('')
    }
  }

  return (
    <Dialog open={open} onOpenChange={() => {}}>
      <DialogContent 
        className="sm:max-w-md"
        onPointerDownOutside={(e) => e.preventDefault()}
        onEscapeKeyDown={(e) => e.preventDefault()}
      >
        <DialogHeader>
          <DialogTitle>Welcome to Jaaz</DialogTitle>
          <DialogDescription>
            Please answer the challenge question to continue
          </DialogDescription>
        </DialogHeader>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="space-y-2">
            <label htmlFor="challenge-answer" className="text-sm font-medium">
              Jaaz is short for...
            </label>
            <Input
              id="challenge-answer"
              type="text"
              value={answer}
              onChange={(e) => setAnswer(e.target.value)}
              placeholder="Enter your answer"
              autoFocus
              autoComplete="off"
            />
            {error && (
              <p className="text-sm text-red-500">{error}</p>
            )}
          </div>

          <Button type="submit" className="w-full">
            Submit
          </Button>
        </form>
      </DialogContent>
    </Dialog>
  )
}
