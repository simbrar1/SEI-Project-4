import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter, Route, Switch } from 'react-router-dom'
import 'spectre.css'

import './style.scss'

import Home from './components/common/Home'
import NavBar from './components/common/NavBar'
import Register from './components/auth/Register'
import Footer from './components/common/Footer'
import Login from './components/auth/Login'

import NewFacts from './components/facts/NewFacts'
import FactsShow from './components/facts/FactsShow'


const App = () => {
  return (
    <BrowserRouter>
      <main>
        <NavBar />
        <Switch>
          <Route path="/register" component={Register} />
          <Route path="/login" component={Login} />
          <Route path="/new/facts" component={NewFacts} />
          <Route path="/facts/:id" component={FactsShow} />
          <Route exact path="/" component={Home} />
        </Switch>
        <Footer />
      </main>
    </BrowserRouter>
  )
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
