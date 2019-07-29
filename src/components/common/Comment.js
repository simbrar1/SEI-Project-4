import React from 'react'

const Comment = ({ text, _id, user, handleCommentDelete, isCommentOwner }) => (
  <div className="card">
    <div className="card-body">{text}</div>
    {isCommentOwner(user) && <button
      className="button"
      onClick={() => handleCommentDelete(_id)}
    >
      Delete Comment
    </button>}
  </div>
)

export default Comment
