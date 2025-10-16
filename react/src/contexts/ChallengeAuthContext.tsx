import { createContext, useContext, useState, ReactNode } from 'react'

interface ChallengeAuthContextType {
  isAuthenticated: boolean
  setAuthenticated: (value: boolean) => void
}

const ChallengeAuthContext = createContext<ChallengeAuthContextType | undefined>(undefined)

export function ChallengeAuthProvider({ children }: { children: ReactNode }) {
  const [isAuthenticated, setIsAuthenticated] = useState(() => {
    // Check sessionStorage on initial load
    return sessionStorage.getItem('jaaz_challenge_authenticated') === 'true'
  })

  const setAuthenticated = (value: boolean) => {
    setIsAuthenticated(value)
    if (value) {
      sessionStorage.setItem('jaaz_challenge_authenticated', 'true')
    } else {
      sessionStorage.removeItem('jaaz_challenge_authenticated')
    }
  }

  return (
    <ChallengeAuthContext.Provider value={{ isAuthenticated, setAuthenticated }}>
      {children}
    </ChallengeAuthContext.Provider>
  )
}

export function useChallengeAuth() {
  const context = useContext(ChallengeAuthContext)
  if (context === undefined) {
    throw new Error('useChallengeAuth must be used within a ChallengeAuthProvider')
  }
  return context
}
