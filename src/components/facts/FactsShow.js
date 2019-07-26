import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import Auth from '../../lib/Auth'


class FactsShow extends React.Component {
  constructor() {
    super()

    this.state = { facts: null}
    this.handleDelete = this.handleDelete.bind(this)
  }

  componentDidMount() {
    axios.get('/api/years')
      .then(res => this.setState({ years: res.data}))
      .catch(err => console.log(err))
  }

  handleDelete() {
    axios.delete(`/api/years${this.props.match.params.id}`, {
      headers: { Authorization: `Bearer ${Auth.getToken()}`}
    })
      .then(() => this.props.history.push('/'))
      .catch(err => console.log(err.response))
  }

  isOwner() {
    return Auth.getPayload().sub === this.state.cheese.user._id
  }


}

export default FactsShow
