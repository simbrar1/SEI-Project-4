import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import Auth from '../../lib/Auth'


class FactsShow extends React.Component {
  constructor() {
    super()

    this.state = { fact: null}
    this.handleDelete = this.handleDelete.bind(this)
  }

  componentDidMount() {
    axios.get(`/api/facts/${this.props.match.params.id}`)
      .then(res => this.setState({ fact: res.data}))
      .catch(err => console.log(err))
  }

  handleDelete() {
    axios.delete(`/api/facts/${this.props.match.params.id}`, {
      headers: { Authorization: `Bearer ${Auth.getToken()}`}
    })
      .then(() => this.props.history.push('/'))
      .catch(err => console.log(err.response))
  }

  isOwner() {
    return Auth.getPayload().sub === this.state.fact.creator.id
  }

  render() {
    if (!this.state.fact) return null
    const { fact } =  this.state
    this.isOwner()
    return (

      <div className="card">

        <div className="card-header">
          <div className="card-title h4">{fact.name}</div>
          <div className="card-subtitle h5">{fact.date_of_fact} {fact.location}</div>
        </div>
        <div className="card-body">
        </div>
        <div className="card-footer">
          <div className="card-title h7">{fact.bio}</div>
        </div>
        <div className="card-image">
          <img src={fact.image} alt={fact.name} className="img-responsive" />
        </div>
        {this.isOwner() && <button onClick={this.handleDelete} className="btn">Delete</button>}
        {this.isOwner() && <button><Link className="button" to={`/facts/${fact.id}/edit`}
        >
        Edit
        </Link></button>}
      </div>
    )
  }


}

export default FactsShow

//took out .id at the end of the is owner
// isOwner() {
//   return Auth.getPayload().sub === this.state.fact.creator.id
